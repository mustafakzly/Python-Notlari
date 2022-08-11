import cv2

image = cv2.imread("resim2.jpg")
hsv_resim = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)    
cv2.namedWindow('HSV resim', cv2.WINDOW_NORMAL)
cv2.imshow('HSV resim', hsv_resim)
cv2.waitKey(0)
#cvtColor() görüntüyü hsv'ye dönüştürdüğümüzü gösterir
x = image.shape
print(x[1])
deger = x[1]-1
for a in range(0,deger): 
        cikti = hsv_resim[a,deger]
        #h 0-178 aralığındaki değerler
        cv2.namedWindow('HSV resim', cv2.WINDOW_NORMAL)
        cv2.imshow('HSV resim', cikti)
cv2.waitKey(0)
cv2.destroyAllWindows()
