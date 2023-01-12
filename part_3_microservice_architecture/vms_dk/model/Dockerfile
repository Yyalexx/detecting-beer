# Задаём базовый образ#
FROM python:3.9
# Задаём рабочую директорию контейнера
WORKDIR /usr/src/app
# Копируем содержимое папки src в рабочую директорию контейнера
COPY ./src ./
# Копируем файл requirements.txt в рабочую директорию контейнера
COPY ./requirements.txt ./
#change to another mirror source
RUN mkdir ~/.pip && \  
cd ~/.pip/  && \  
echo "[global] \ntrusted-host =  pypi.douban.com \nindex-url = http://pypi.douban.com/simple" >  pip.conf
# Устанавливаем зависимости
RUN pip install -r requirements.txt
# Исполняем команду для запуска скрипта
CMD [ "python", "./model.py" ]
