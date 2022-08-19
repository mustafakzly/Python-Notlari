import cv2
import os

#buraya dosya yolunu koydum
path = "C:/Users/Mustafa/Desktop/Python/OpenCV/"

for resim in os.listdir(path):
    if resim.endswith('.jpg'):
        img = cv2.imread(resim)
        cv2.namedWindow("goruntu",cv2.WINDOW_NORMAL)
        cv2.imshow("goruntu", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        