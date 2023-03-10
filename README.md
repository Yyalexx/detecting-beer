# ТЕМА ПРОЕКТА  
## Определение количества позиций товара на витрине по фотографиям. 
(python, json, numpy, pandas, PIL, torch, yolov5, pika, RabbitMQ, Docker Compose)
## ПОСТАНОВКА ЗАДАЧИ

<img align="right" width="154" height="205" src=img/4.jpg>

Заказчиком является торговая фирма - генеральный дистрибьютор производителя пива и крекера [ОАО ВИЗИТ](https://www.vizitbeer.ru/).


Мерчендайзеры фирмы ежедневно обходят закрепленные за ними торговые точки и в виде отчета делают фотографии витрин. Фотографии загружаются в базу данных 1С и визуально анализируются руководителем службы.

В этом проекте в целях автоматизации анализа отчетов мерчендайзеров производится подсчет количества позиций в первом ряду витрины единицы анализируемого ассортимента на каждой фотографии.  


## Проект состоит из 3-х частей:

- [Часть 1: Разметка данных](https://github.com/Yyalexx/detecting-beer/tree/master/part_1_data_labeling)
- [Часть 2: Тренировка модели](https://github.com/Yyalexx/detecting-beer/tree/master/part_2_model_training)  
- [Часть 3: Сервис (продакшн)](https://github.com/Yyalexx/detecting-beer/tree/master/part_3_microservice_architecture)  
### [Часть 1: Разметка данных](https://github.com/Yyalexx/detecting-beer/tree/master/part_1_data_labeling)  
<img align="right" width="154" height="154" src=./img/predict_samples/18.jpg>  

Для разметки данных используется библиотека [label-studio](https://labelstud.io/) .
### [Часть 2: Тренировка модели](https://github.com/Yyalexx/detecting-beer/tree/master/part_2_model_training)  
Для обучения была выбрана модель YOLOv5 от разработчика [ultralytics](https://ultralytics.com/).  
### [Часть 3: Сервис (продакшн)](https://github.com/Yyalexx/detecting-beer/tree/master/part_3_microservice_architecture)  
Реализована микросервисная структура из 3-х сервисов с контейнеризацией Docker Compose.  
## Промежуточные выводы  
- Применение модели YOLOv5 продемонстрировало свою эффективность для поставленной задачи. 
- Применение микросервисной структуры позволяет оперативно добавлять анализируемые товарные позиции.  
## Основные итоги  
- Создана микросервисная структура, инференс в реальном времени в автоматическом режиме анализирует количество позиций в первом ряду витрины одной единицы ассортимента.  
- Система полностью готова к расширению анализируемого ассортимента.
- Определены конкретные задачи по развитию системы как в направлении расширения количества ассортиментных позиций, так и в направлении дальнейшего развития сервиса.  
  
## Деплой прототипа на **Streamlit Cloud**  
<img align="" width="1000" height="" src=./img/predict_samples/demo.gif>  

### Update 21.02.2023  
Всего обучено 6 моделей на 15 классов.
### Update 17.02.2023  
Всего обучено 5 моделей на 12 классов.
### Update 7.02.2023
Всего обучено 4 модели на 10 классов.
### Update 17.01.2023  
Размечены данные для класса "Визит вечерний стекло 0.45", обучена модель.  
Добавлены файлы *demo_predict_cl_0_1.ipynb* и *m_cl_1.pt*.  
### Пример работы модели на тестовых данных

<img align="" width="400" height="" src=./img/predict_samples/20.jpg> 
  
  ### Update 19.01.2023  
Размечены данные для класса "Визит классический ПЭТ 1.5л", обучена модель *m_cl_1_2.pt* на два класса:  
- "Визит классический ПЭТ 1.5л"
- "Визит вечерний стекло 0.45".  
Добавлены файлы *demo_predict_cl_0_1_2.ipynb* и *m_cl_1_2.pt*.  
### Примеры работы модели на тестовых данных

<img align="" width="400" height="" src=./img/predict_samples/27.jpg> 
<img align="right" width="400" height="" src=./img/predict_samples/25.jpg> 
<img align="" width="400" height="" src=./img/predict_samples/26.jpg> 
<img align="right" width="400" height="" src=./img/predict_samples/24.jpg> 
