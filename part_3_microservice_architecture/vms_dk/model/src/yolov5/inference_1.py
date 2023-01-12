import os 
import shutil 
import glob
from tqdm import tqdm
from PIL import Image
import pyautogui

path_to_files = "b:/VIZIT/yolov5"
input_image_path = "b:/VIZIT/yolov5/CHECK_photo"

# Функция для изменения размеров изображения и переноса изображения и labels в папку resized
def scale_image(input_image_path,
                      width=640,
                      height=640, 
                      PATH=path_to_files
                      ):

    path_to_resized_images = ''.join((PATH, '/resized_images/'))
    
    
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    
    if hasattr(original_image, '_getexif') or original_image._getexif() is not None:
        orientation = original_image._getexif().get(0x112)
        rotate_values = {3: 180, 6: 270, 8: 90}
        if orientation in rotate_values:
            img = resized_image.rotate(rotate_values[orientation])
        else:
            img = resized_image    
        
    resized_image_path = ''.join((path_to_resized_images, input_image_path.split('\\')[-1]))
    img.save(resized_image_path)


# Преобразованные файлы изображений
path_to_resized_images = ''.join((path_to_files, '/resized_images/'))

if os.path.exists(path_to_resized_images):
    shutil.rmtree(path_to_resized_images)
os.mkdir(path_to_resized_images)
    
img_names_list = glob.glob(input_image_path +'/*.jpg')    
for img_name in tqdm(img_names_list):
    scale_image(img_name)
    
    
#$ pip install requirements.txt

python detect.py --weights b:/VIZIT/yolov5/best.pt --img 640 --conf 0.1 --source b:/VIZIT/yolov5/resized_images  --line-thickness 1 --hide-labels --save-txt

n_photos = len(glob.glob(input_image_path +'/*.jpg'))

while True:
    a = pyautogui.confirm(text= f"Вывести {n_photos} фото на экран ?", title='Визуализация', buttons=['Да', 'Нет'])
    
    if a=='Да':
        from IPython.display import Image, display
        path_inference = glob.glob("b:/VIZIT/yolov5/runs/detect/*")[-1]
        glob.glob(path_inference+'/*.jpg')

        for imageName in glob.glob(path_inference+'/*.jpg'): #assuming JPG
            display(Image(filename=imageName))
            print("\n")
        break
    elif a=='Нет':
        break