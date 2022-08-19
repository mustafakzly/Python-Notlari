import cv2
import numpy as np

img1 = cv2.imread("limon.jpg")
img2 = cv2.imread("manzara.jpg")
img1 = cv2.resize(img1,(300,300))


x,y,z = img1.shape
roi = img2[0:x,0:y]

img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img1_gray,190,255,cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg = cv2.bitwise_and(img1,img1,mask=mask)

toplam = cv2.add(img1_bg,img2_fg)

img2[0:x,0:y] = toplam
cv2.namedWindow("resim",cv2.WINDOW_NORMAL)
cv2.imshow("resim",img2)
cv2.imshow("resim2",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows() 



# img1 = cv2.imread("manzara.jpg")
# img2 = cv2.imread("limon.jpg")

# toplam = cv2.addWeighted(img1,0.7,img2,0.3,0)
# #iki resmi üst üste ekleme
# cv2.imshow("resim",toplam)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 