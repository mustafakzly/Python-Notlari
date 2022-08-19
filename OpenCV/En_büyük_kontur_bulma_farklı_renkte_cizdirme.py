import cv2
import time

baslangic_zamani = time.time()
#Zamanı bir başlangıç zamanının içine atadım uygulama çalıştığında kayıt edecek

img = cv2.imread("limon.jpg")
#Resmi okudum

img = cv2.resize(img,(500,500))
#Fotoğrafı 500x500 formatına dönüştürdüm

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
#Resmi gri formata dönüştürdüm

alt_esik = 50
üst_esik = 255
#Cannyde kullanacağımız alt ve üst eşiği belirttik

cerceveli = cv2.Canny(gray,alt_esik,üst_esik)
#Canny algoritması kullanarak resimdeki köşeleri bulduk

contours, hierarchy = cv2.findContours(cerceveli,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)         
print("kontur sayısı: ", len(contours))
#Contours uygulamasıyla kaç tane contours olduğunu bulduk.

for i in range(0,len(contours)):
    if 300 < len(contours[i]):
        print("En büyük contours: ", i)
        cv2.drawContours(img, contours[i], -1,(0,0,255),10)
#Bu dizide en büyük contoursu bulduk ve çizdirdik   


#Contours çizdirerek bulduğumuz köşegenleri işaretledik.


cv2.imshow("Contours",img)
#Çıkan sonuçları gösterttik

cv2.waitKey(0)
#Kapanmaması için waitKey'e 0 değerini verdik.

cv2.destroyAllWindows()                                 

gecenSure = (time.time()- baslangic_zamani)*1000
print("GEÇEN SÜRE : ", gecenSure ,"ms")
#Burada da girişte aldığımız süreyi uygulama bittiğindeki süreyle çıkarıp kaç sn geçtiğini bulduk