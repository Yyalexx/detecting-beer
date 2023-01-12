import pika
import json
from PIL import Image
import glob
import time
import os
import os.path
import shutil

path_to_volume = './vvol/'

print('...Waiting for images to be processed, click CTRL+C to exit')

# Очищаем папку resized_images при запуске сервиса
path_to_resized_images = path_to_volume +'resized_images/'
if os.path.exists(path_to_resized_images):
    shutil.rmtree(path_to_resized_images)
os.mkdir(path_to_resized_images)

while True:

    try:
        #Функция для изменения размеров изображения и переноса изображения в папку resized
        def scale_img(input_image_path,
                        path_to_volume=path_to_volume):

            img_id = input_image_path.split('/')[-1][:-4]
            path_to_resized_img = path_to_volume +'resized_images/'+img_id+'.jpg' 
            original_image = Image.open(input_image_path)
            resized_image = original_image.resize((640, 640), Image.LANCZOS)
            
            if hasattr(original_image, '_getexif') or original_image._getexif() is not None:
                orientation = original_image._getexif().get(0x112)
                rotate_values = {3: 180, 6: 270, 8: 90}
                if orientation in rotate_values:
                    img = resized_image.rotate(rotate_values[orientation])
                else:
                    img = resized_image 
            img.save(path_to_resized_img)
            msg_dict = {'id': img_id,'body': path_to_resized_img}
            
            return msg_dict

        inp_img_list = glob.glob(path_to_volume+'input_images/*.jpg')
        
        #Подключение к серверу на локальном хосте:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        #Создаём очередь images
        channel.queue_declare(queue='images')

        # 
        for inp_img in inp_img_list:
            
            msg = scale_img(inp_img)

            # Публикуем сообщение в очередь images
            channel.basic_publish(exchange='',
                            routing_key='images',
                            body=json.dumps(msg))
            print('Message with image path sent to queue')
            # Удаляем изображение из папки input_images
            os.remove(inp_img)

        # Закрываем подключение
        connection.close()
    except:
        print('Failed to connect to the queue')
    time.sleep(10)