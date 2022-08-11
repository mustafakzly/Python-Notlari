import cv2
import numpy as np

img = np.zeros([512,512,3],np.uint8)
#çizgi
cv2.line(img,(0,0),(511,511),(255,0,0),5) # (verilen resim adı , x kordinatları , y kordinatları , renk), çizgi kalınlığı
cv2.line(img,(511,0),(0,511),(0,0,255),5)
#kare
cv2.rectangle(img,(50,50),(300,300),(0,0,255),5)
cv2.rectangle(img,(300,300),(511,511),(0,0,255),-1) # -1 karenin içini doldurur
#daire
cv2.circle(img,(255,255),60,(120,120,120),5) # resim , merkezi , yarıçapı , renk , kalınlık
cv2.circle(img,(100,100),90,(190,190,190),-1)
#elipse
cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,100,0),3) # resim , merkez , uzunluk, yayın_açısı başlangıç ve bitiş , reng , kalınlıki
cv2.ellipse(img,(100,100),(100,50),0,0,180,(255,100,0),-1)

pts = np.array([[20,30],[100,120],[255,255],[10,400]],np.int32)
pts2 = pts.reshape(-1,1,2)
cv2.polylines(img, [pts], True , (255,255,255),3)
#yazı yazma
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"opencv",(15,256),font,4,(0,255,255),2,cv2.LINE_AA) # resim , yazı , korinat , font,boyut , renk , kalınlık

cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()