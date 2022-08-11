import cv2
import os

for resim in os.listdir("C:/Users/Mustafa/Desktop/Python/OpenCV/Deneme1/"):
    
    if resim.endswith('.jpg'):
       img = cv2.imread(resim)
       # cv2.imshow("img",img)
       # cv2.waitKey(1000)
       
       