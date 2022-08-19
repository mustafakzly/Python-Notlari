import cv2

img = cv2.imread("resim3.jpg")
img = cv2.resize(img,(1280,720))
rows , cols ,_ = img.shape
print(rows,cols)



font = cv2.FONT_HERSHEY_COMPLEX
x=0
y = 50
for i in range(0, rows-1):
    for j in range(0, cols-1):
        img = cv2.imread("resim3.jpg")
        cv2.putText(img,"MUSTAFA",(x,y),font,2,(0,x%255,y%100),1,cv2.LINE_AA)
        x += 50
        if x > 1280:
            y += 50
            x = 0
        cv2.imshow("resim",img)
        cv2.waitKey(10)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        

cv2.destroyAllWindows()