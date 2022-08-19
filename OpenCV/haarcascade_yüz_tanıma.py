import cv2


face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#haarcascade dosyasını tamıladık

image = cv2.imread("people.jpg")
#yüz bulacağımız fotoğrafı okuduk

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#Fotoğrafı gri formata dönüştürdük

faces = face_classifier.detectMultiScale(gray,1.2,7)
#fotoğraftaki yüzleri bulmak için faces diye tanımlama yaptık ve içine yüzleri aktardık.

if faces is ():
    print("yüz bulunamadı.")
#eğer yüz yoksa yüz bulunamadı yazdırdık

for (x,y,w,h) in faces:
    #for döngüsünde x,y,w,h kordinatlarını yüzde bulduk
    
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    #bulduğumuz kordinatlardaki yüzleri kare içerisine aldırdık
    
    print(f"x : {x} , y : {y} , w : {w} , h : {h}")
    #Görmek için x,y,w,h kordinatlarını yazdırdım
    yuz = image[y:y+h,x:x+w]
    
    cv2.imshow('kesilen_yuz', yuz) 
    cv2.waitKey(0)
# cv2.imshow('bulunan yuz', image) 
# cv2.imshow('kesilen_yuz', yuz)
# cv2.waitKey(0)
cv2.destroyAllWindows()