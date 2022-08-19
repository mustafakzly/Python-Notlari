import os
import cv2
import shutil

yeni_dosya = os.mkdir("2400_3875_images")
yeni_dosya1 = os.mkdir("1920_1280_images")
yeni_dosya2 = os.mkdir("640_960_images")
# 3 adet yeni dosya ekledik
klasor = os.listdir("C:/Users/Mustafa/Desktop/Python/OpenCV/images")



for i in range(0,len(klasor)):
    img2 = cv2.imread(f"C:/Users/Mustafa/Desktop/Python/OpenCV/images/{klasor[i]}")
    cols,rows,_ = img2.shape
    print(f"sütun = {cols} , satır = {rows} ")
    if  cols >= 3600:
        shutil.move(f"C:/Users/Mustafa/Desktop/Python/OpenCV/images/{klasor[i]}","2400_3875_images")
        
    elif  cols >= 1200 and cols < 3600:
        
        shutil.move(f"C:/Users/Mustafa/Desktop/Python/OpenCV/images/{klasor[i]}","1920_1280_images")
        
    elif  cols < 1200 :
        
        shutil.move(f"C:/Users/Mustafa/Desktop/Python/OpenCV/images/{klasor[i]}","640_960_images")
