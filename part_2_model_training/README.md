# Обучение модели 
Исходная задача представляет собой задачу object-detection. 
Было принято решение использовать YOLO. Это популярная архитектура CNN для решения задачи object-detection. В настоящее время можно найти много описаний и примеров практического применения в интернете.  
Основная идея YOLO состоит в том, что нейросеть обрабатывает всё входное изображение лишь единожды. Такой подход дает существенный выигрыш в быстродействии по сравнению с методами, где происходит несколько независимых классификаций выделенных областей изображения.   
Для обучения была выбрана модель YOLOv5 от разработчика [ultralytics](https://ultralytics.com/). YOLOv5 - это семейство архитектур и моделей обнаружения объектов, предварительно обученных на наборе данных COCO и реализованых с использованием фреймворка Pytorch. Проект, выложенный на [github ultralytics](https://github.com/ultralytics/yolov5), содержит подробные инструкции для обучения модели на данных, которые не содержатся в датасете COCO ("Custom Data"), инструкции по заморозке слоев при transfer learning, ансамблированию и TTA во время тестирования и инференса модели и т.п. Для обучения модели использовалась инструкция ["Train Custom Data"](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data) с использованием [ноутбука в Google Colab](https://colab.research.google.com/github/roboflow-ai/yolov5-custom-training-tutorial/blob/main/yolov5-custom-training.ipynb). 
 
Обучение модели данного проекта производится в ноутбуке Google Colab. Импортированный ноутбук **model_training.ipynb** представлен в данном разделе.  
Предварительная обработка данных заключается в придании размера, необходимого для обучения нейронной сети, и правильной ориентации.  
После этого этапа данные разбиваются на тренировочную, валидационную и тестовую выборки. Для размещения выборок в библиотеке YOLO предусмотрена соответствующая структура папок, которая и создается далее в ноутбуке.  
Вего было размечено 530 фотографий. Первоначально они были разбиты на части в пропорции 70% - тренировочная выборка, валидационная и тестовая по 15% соответственно. Обучение и валидация модели показали отсутствие переобучения. Так как для качества обучения важен размер тренировочной выборки, а разметка весьма трудоемка, пропорция разбиения на выборки для последующего обучения была изменена на 90%, 5% и 5% соответственно для увеличения тренировочной выборки.  
В соответствии с [инструкцией](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data) 
<img align="right" width="400" height="" src=../img/yolo_models.png>  
первоначально для *baseline* была выбрана модель YOLOv5s, но потом была она была заменена на модель YOLOv5m, которая обеспечила достаточно хорошее качество детекции объектов.
После обучения модели на валидационной выборке были получены следующие значения основных метрик:  
- precision - 0.961  
- recall - 0.956


### Визуализация метрик с использованием платформы [TensorFlow](https://www.tensorflow.org/)  
<img align="" width="600" height="" src=../img/metrics/1.png>  

<img align="" width="600" height="" src=../img/metrics/2.png>  

<img align="" width="600" height="" src=../img/metrics/3.png>  

<img align="" width="600" height="" src=../img/metrics/4.png>  

<img align="" width="400" height="" src=../img/metrics/5.png>  

<img align="" width="400" height="" src=../img/metrics/6.png>  

<img align="" width="400" height="" src=../img/metrics/7.png>  

<img align="" width="400" height="" src=../img/metrics/8.png>  


# Демонстрация работы модели на тестовых данных  
Для визуализации результатов детекции объектов было проведено предсказание на тестовой выборке штатными средствами YOLO в ноутбуке **demo_predict.ipynb**, представленном в этой папке. На обработанные фото нанесены результаты детекции объектов в виде рамок.


### Примеры работы модели на тестовых данных

<img align="" width="400" height="" src=../img/predict_samples/1.jpg> 
<img align="right" width="400" height="" src=../img/predict_samples/2.jpg> 
<img align="" width="400" height="" src=../img/predict_samples/3.jpg> 
<img align="right" width="400" height="" src=../img/predict_samples/4.jpg> 
<img align="" width="400" height="" src=../img/predict_samples/5.jpg> 
<img align="right" width="400" height="" src=../img/predict_samples/6.jpg> 
<img align="" width="400" height="" src=../img/predict_samples/7.jpg> 
<img align="right" width="400" height="" src=../img/predict_samples/8.jpg> 
<img align="" width="400" height="" src=../img/predict_samples/9.jpg> 
<img align="right" width="400" height="" src=../img/predict_samples/10.jpg> 
<img align="" width="400" height="" src=../img/predict_samples/11.jpg> 
<img align="right" width="400" height="" src=../img/predict_samples/12.jpg> 
<img align="" width="400" height="" src=../img/predict_samples/13.jpg> 
<img align="right" width="400" height="" src=../img/predict_samples/14.jpg> 
<img align="" width="400" height="" src=../img/predict_samples/15.jpg>
<img align="right" width="400" height="" src=../img/predict_samples/16.jpg>  
<img align="" width="400" height="" src=../img/predict_samples/17.jpg> 
<img align="right" width="400" height="" src=../img/predict_samples/18.jpg> 