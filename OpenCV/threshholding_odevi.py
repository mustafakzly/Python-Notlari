import cv2
import matplotlib as plt
img = cv2.imread("limon.jpg",0)
#resmi okuduk ve 2. parametreye yazdığımız 0 la grileştirdik
image = cv2.resize(img,(800,500))
#Resim büyük olduğu için resize ederek boyutunu ayarladım
blur = cv2.GaussianBlur(image, (5,5), 0)

# ret,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,thresh = cv2.threshold(blur,190,255,cv2.THRESH_BINARY)
# adathresh_mean = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)

cv2.imshow("original",image)
cv2.imshow("thersh",thresh)
cv2.imshow("adaptive",adathresh_mean)
cv2.waitKey(0)
cv2.destroyAllWindows()