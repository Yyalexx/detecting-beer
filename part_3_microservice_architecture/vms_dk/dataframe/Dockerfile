# Задаём базовый образ#
FROM python:3.9
# Задаём рабочую директорию контейнера
WORKDIR /usr/src/app
# Копируем содержимое папки src в рабочую директорию контейнера
COPY ./src ./
# Копируем файл requirements.txt в рабочую директорию контейнера
COPY ./requirements.txt ./
# Устанавливаем зависимости
RUN pip install -r requirements.txt
# Исполняем команду для запуска скрипта
CMD [ "python", "./dataframe.py" ]
