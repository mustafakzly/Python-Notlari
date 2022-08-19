import os
import shutil

yeni_dosya = os.mkdir("2400_3875_images")
yeni_dosya1 = os.mkdir("1920_1280_images")
yeni_dosya2 = os.mkdir("640_960_images")
klasor = os.listdir("C:/Users/Mustafa/Desktop/Python/OpenCV/images")

for i in range(0,20):
     deger = int(os.stat(f"{klasor[i]}").st_size/1024)
     if deger > 680 and deger < 2000:
         
         shutil.move(f"C:/Users/Mustafa/Desktop/Python/OpenCV/images/{klasor[i]}","2400_3875_images")
     elif deger < 680 and deger > 200 :
         
         shutil.move(f"C:/Users/Mustafa/Desktop/Python/OpenCV/images/{klasor[i]}","1920_1280_images")
     elif deger < 90 and deger >10:
         
         shutil.move(f"C:/Users/Mustafa/Desktop/Python/OpenCV/images/{klasor[i]}","640_960_images")