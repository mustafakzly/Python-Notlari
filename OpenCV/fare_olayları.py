import cv2
import numpy as np
"""
img = np.ones((512,512,3),np.uint8)

def draw(event, x , y , flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(255,0,0),3)
    pass

cv2.namedWindow("point")
cv2.setMouseCallback("point",draw)

while(1):
    cv2.imshow("point",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
"""
cizim = False
mod = False
xi,yi = -1,-1
def draw(event, x , y , flags, param):
   global cizim,xi,yi,mod
   if event == cv2.EVENT_LBUTTONDOWN:
       xi,yi = x,y
       cizim = True
   elif event == cv2.EVENT_MOUSEMOVE:
       if cizim == True:
           if mod:
               cv2.circle(img,(xi,yi),10,(100,50,0),2)
           else:
               cv2.rectangle(img,(xi,yi),(x,y),(0,0,255),3)
       else:
           pass
   elif event == cv2.EVENT_LBUTTONUP:
       pass

img = np.ones((512,512,3),np.uint8)



cv2.namedWindow("point")
cv2.setMouseCallback("point",draw)

while(1):
    cv2.imshow("point",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if cv2.waitKey(1) & 0xFF == ord("m"):
       mod = not mod
cv2.destroyAllWindows()