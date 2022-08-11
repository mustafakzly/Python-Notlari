import cv2
import numpy as np

image = cv2.imread("groot.jpg")
r_image = cv2.resize(image,(500,800))
gray = cv2.cvtColor(r_image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)


canny = cv2.Canny(blur,50,150)
# 1. parametre kullanılması istenilen resim , 2. parametre alt eşik değeri , 3. parametre üst eşik değeri



cv2.imshow("blur",blur)
cv2.imshow("canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()


#otomatik canny algoritması
"""
def autoCanny(blur, sigma = 0.33):
    median = np.median(blur)
    lower = int(max(0,(1.0-sigma)*median))
    upper = int(min(255,(1.0+sigma)*median))
    canny = cv2.Canny(blur,lower,upper)
    
    return canny
wide = cv2.Canny(blur,10,220)
tight = cv2.Canny(blur,200,300)
auto = autoCanny(blur)

cv2.imshow("blur",auto)
cv2.imshow("edges",np.hstack([wide,tight,auto]))
cv2.waitKey(0)
cv2.destroyAllWindows()
"""