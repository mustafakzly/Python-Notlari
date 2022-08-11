import cv2

img = cv2.imread("resim1.jpg")
img = cv2.resize(img,(500,500))
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray,50,200)

cv2.imshow("Edged",edged)

contours, hierarchy = cv2.findContours(edged,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                                            #Hiyerarşi değeri ile ilgili bilgiler tutar, Kontur yaklaşım methodu değerlerini tutar
cv2.drawContours(img, contours, -1,(255,0,0),4)  #-1 tüm konturlar demek          

cv2.imshow("Contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()                                 