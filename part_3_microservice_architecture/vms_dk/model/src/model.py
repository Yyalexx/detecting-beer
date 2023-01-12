import pika
import json
import numpy as np
import torch
from PIL import Image
import os
import os.path

# Списки обрабатываемых классов для моделей
model_1_class_list = [0]
model_2_class_list = [1,2,3,4]
# Модели для обрабатываемых классов
model_1 = torch.hub.load('./yolov5', 'custom', path='./model_cl_0.pt', 
            source='local', device='cpu', force_reload=True, _verbose=False)
model_2 = torch.hub.load('./yolov5', 'custom', path='./model_cl_1_4.pt', 
            source='local', device='cpu', force_reload=True, _verbose=False)

try:
    # Создаём подключение к серверу на локальном хосте:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    # Объявляем очередь images
    channel.queue_declare(queue='images')
    # Объявляем очередь predict
    channel.queue_declare(queue='predict')

    import shutil
    # Создаём функцию callback для обработки данных из очереди images
    def callback(ch, method, properties, body):
        print(f'Image received for processing {body}')
        path_to_img =  json.loads(body)['body']
        img = Image.open(path_to_img)
        img_id = json.loads(body)['id']
        
        d={}  # Словарь предиктов всех обрабатываемых классов
        # Заполняем словарь предиктов предиктами первой модели
        results = model_1(img, size=640)
        col_class=results.xyxy[0][:,5]
        for cls in model_1_class_list:
            d[cls] = len(np.where(col_class==cls)[0])
        # Заполняем словарь предиктов предиктами второй модели
        results = model_2(img, size=640)
        col_class=results.xyxy[0][:,5]
        for cls in model_2_class_list:
            d[cls] = len(np.where(col_class==cls)[0])
        # Преобразуем словарь предиктов в список
        curr_cl_list = []
        for i in range(len(list(d.keys()))):
            curr_cl_list.append(d[i])
        msg = {'id': img_id, 'body': curr_cl_list}
        # Публикуем сообщение в очередь predict
        channel.basic_publish(exchange='',
                        routing_key='predict',
                        body=json.dumps(msg))
        print(f'Prediction {msg} sent to predict queue')
        # Удаляем изображение из папки resized
        os.remove(path_to_img)

    # Извлекаем сообщение из очереди images
    channel.basic_consume(
        queue='images',
        on_message_callback=callback,
        auto_ack=True
    )
    print('...Waiting for messages, press CTRL+C to exit')

    # Запускаем режим ожидания прихода сообщений
    channel.start_consuming()
except:
    print('Failed to connect to the queue')