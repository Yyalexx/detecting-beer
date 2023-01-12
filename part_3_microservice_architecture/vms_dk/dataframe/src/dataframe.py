import pika
import pandas as pd
import json
import os
import os.path

path_to_volume = './vvol/'
path_to_df = path_to_volume+'predict_df.csv'

col_list = ['img_id']
col_list.extend(list(range(5)))

try:
    # ПРОВЕРКА ПРИ ЗАПУСКЕ СЕРВИСА
    # Если файл таблицы существует, удаляем его
    if os.path.isfile(path_to_df):
        # Считываем таблицу из файла
        os.remove(path_to_df)
    
        # Создаем таблицу таблицу
    predict_df = pd.DataFrame(columns=col_list)


    # Создаём подключение к серверу на локальном хосте
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    # Объявляем очередь predict
    channel.queue_declare(queue='predict')

    # Создаём функцию callback для обработки данных из очереди
    def callback(ch, method, properties, body):
        predict_list = [json.loads(body)['id']]
        predict_list.extend(json.loads(body)['body'])
        print(f'Value {json.loads(body)} received from queue {method.routing_key}')
        predict_df.loc[len(predict_df.index)] = predict_list
        predict_df.drop_duplicates(subset=['img_id'], inplace=True)
        predict_df.to_csv(path_to_df, index=False)

    # Извлекаем сообщение из очереди predict
    channel.basic_consume(
        queue='predict',
        on_message_callback=callback,
        auto_ack=True
        )


    # Запускаем режим ожидания прихода сообщений
    print('...Waiting for messages, press CTRL+C to exit')
    channel.start_consuming()
except:
    print('Failed to connect to the queue')


