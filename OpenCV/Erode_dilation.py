import cv2
import numpy as np

img = cv2.imread("yildiz.jpg")
matris = np.ones((5, 5), np.uint8)

img_erode = cv2.erode(img, matris, iterations=1)
img_dilate = cv2.dilate(img, matris, iterations=1)
cv2.namedWindow('ilk',cv2.WINDOW_NORMAL)
cv2.namedWindow('Erode',cv2.WINDOW_NORMAL)
cv2.namedWindow('Dilate',cv2.WINDOW_NORMAL)
cv2.imshow('ilk', img)
cv2.imshow('Erode', img_erode)
cv2.imshow('Dilate', img_dilate)
 
cv2.waitKey(0)
cv2.destroyAllWindows()

#erode ön plandaki nesnenin kalınlığı veya boyutu azalır, görüntüdeki beyaz bölge azalır
#dilate görüntüdeki beyaz bölgeyi artırır kırık parçaların birleştirilmesinde de yararlıdır.