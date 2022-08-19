import cv2
import numpy as np

image = cv2.imread("groot.jpg")
r_image = cv2.resize(image,(500,800))
gray = cv2.cvtColor(r_image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)
tlower = 50
tupper = 150
matris = np.ones((tlower, tupper), np.uint8)

img_erod = cv2.erode(image, matris, iterations=1)
img_dilat = cv2.dilate(image, matris, iterations=1)

canny = cv2.Canny(blur,tlower,tupper)
# 1. parametre kullanılması istenilen resim , 2. parametre alt eşik değeri , 3. parametre üst eşik değeri



cv2.imshow("blur",blur)
cv2.imshow("canny",canny)
cv2.imshow("erod",img_erod)
cv2.imshow("dilat",img_dilat)
cv2.waitKey(0)
cv2.destroyAllWindows()
