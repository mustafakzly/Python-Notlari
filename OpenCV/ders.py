import cv2

#video çekme
cam = cv2.VideoCapture(0)
fourrc = cv2.VideoWriter_fourrc(*'XVID')

out = cv2.VideoWriter("dronegri.avi",fourrc,30.0,(640,480))

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        print("kameradan görüntü alınamadı.")
        break
    out.write(frame)
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1) == ord("q"):
        print("videodan ayrıldınız.")
        break
    
cam.release()
out.release()
cv2.destroyAllWindows()

"""
#video izleme
cam = cv2.VideoCapture("drone.mp4")

while cam.isOpened():
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if not ret:
       print("cameradan görüntü okunamıyor.")
    cv2.imshow("görüntü",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("video sonlandırıldı.")
        break
"""
'''
#camera açma
cam = cv2.VideoCapture(0)

print(cam.get(3))
print(cam.get(4))

cam.set(3,320)
cam.set(4,240)

print(cam.get(3))
print(cam.get(4))
if cam.isOpened():
    print("kamera tanınmadı.")
while True:
    ret,frame = cam.read() # ret true ya da false değeri , frame resim çerçevesi verir
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #cv2.COLOR_BGR2GRAY görüntü siyah beyaz yapar
    if not ret:
        print("cameradan görüntü okunamıyor.")
        break
    cv2.imshow("kamera",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Görüntü sonlandırıldı.")
        break

cam.release()
cv2.destroyAllWindows()
'''

"""
import numpy as np

sifir = np.zeros([300,300])
bir = np.ones([300,300])

cv2.namedWindow("sifir",cv2.WINDOW_NORMAL)
cv2.namedWindow("bir",cv2.WINDOW_NORMAL)
cv2.imshow("sifir",sifir)
cv2.imshow("bir",bir)

cv2.waitKey(0)

cv2.destroyAllWindows()
"""