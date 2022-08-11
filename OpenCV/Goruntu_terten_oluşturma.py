import cv2
import numpy as np
img = cv2.imread("resim1.jpg")
bit_not = cv2.bitwise_not(img)
cv2.namedWindow("goruntu",cv2.WINDOW_NORMAL)

cv2.imshow("goruntu",bit_not)

cv2.waitKey(0)

