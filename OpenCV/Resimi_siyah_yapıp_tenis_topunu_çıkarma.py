import cv2

def nothing(x):
    pass

img = cv2.imread("tenis.jpg")
cv2.namedWindow("resim",cv2.WINDOW_NORMAL)

cv2.createTrackbar("H","resim",0,178,nothing)
cv2.createTrackbar("S","resim",0,255,nothing)
cv2.createTrackbar("V","resim",0,255,nothing)

while(1):
    
    cv2.imshow("resim",img)
    
    if cv2.waitKey(1) & 0xFF == ("q"):
        break
    h = cv2.getTrackbarPos("H","resim")
    s = cv2.getTrackbarPos("S","resim")
    v = cv2.getTrackbarPos("V","resim")
    
    img[:-1] = [h,s,v]
cv2.waitKey(0)
cv2.destroyAllWindows()