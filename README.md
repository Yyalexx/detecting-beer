# ТЕМА ПРОЕКТА  
## Определение количества товарных позиций по фотографиям витрин. 
(python, json, numpy, pandas, PIL, torch, yolov5, pika, RabbitMQ, Docker Compose)
## ПОСТАНОВКА ЗАДАЧИ

<img align="right" width="154" height="205" src=images/49124b47-d05b-31dc-fad5-cd51839515be.jpg>

Заказчиком является торговая фирма - генеральный дистрибьютор производителя пива и крекера [ОАО ВИЗИТ](https://www.vizitbeer.ru/).


Мерчендайзеры фирмы ежедневно обходят закрепленные за ними торговые точки и в виде отчета делают фотографии витрин. Фотографии загружаются в базу данных 1С и визуально анализируются руководителем службы.

В в этом проекте целях автоматизации анализа фотографий производится подсчет количества товарных позиций интересующего ассортимента на каждой фотографии.

## Проект состоит из 3-х частей:
- [Часть 1: Разметка данных](https://github.com/Yyalexx/detecting-beer/tree/master/part_1_data_labeling)
- [Часть 2: Тренировка модели](https://github.com/Yyalexx/detecting-beer/tree/master/part_2_model_training)  
- [Часть 3: Сервис](https://github.com/Yyalexx/detecting-beer/tree/master/part_3_microservice_architecture)  
### [Часть 1: Разметка данных](https://github.com/Yyalexx/detecting-beer/tree/master/part_1_data_labeling)  
Для разметки данных используется библиотека [label-studio](https://github.com/heartexlabs/label-studio) .
### [Часть 2: Тренировка модели](https://github.com/Yyalexx/detecting-beer/tree/master/part_2_model_training)  
Для обучения была выбрана модель YOLOv5 от разработчика [ultralytics](https://ultralytics.com/).  
### [Часть 3: Сервис](https://github.com/Yyalexx/detecting-beer/tree/master/part_3_microservice_architecture)  
Реализована микросервисная структура из 3-х сервисов с контейнеризацией Docker Compose.