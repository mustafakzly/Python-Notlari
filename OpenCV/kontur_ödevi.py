import cv2
import time
baslangic_zamani = time.time()
img = cv2.imread("limon.jpg")
img = cv2.resize(img,(500,500))
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
cerceveli = cv2.Canny(gray,50,255)



contours, hierarchy = cv2.findContours(cerceveli,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)         
print("kontur sayısı: ", len(contours))

cv2.drawContours(img, contours, -1,(255,0,0),4)
cv2.imshow("Edged",cerceveli)
cv2.imshow("Contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()                                 

gecenSure = int((time.time()- baslangic_zamani))
print("GEÇEN SÜRE : ", gecenSure ,"saniye")