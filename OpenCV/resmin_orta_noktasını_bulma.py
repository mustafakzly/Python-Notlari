import cv2

img = cv2.imread("resim2.jpg",0)
#öncelikle resmi okuyoruz.
rows , cols = img.shape
#burada satır ve sütünların hangi uzunlukta olduklarını buluyoruz.
x = int((rows/2))
y= int((cols/2))
print(int(img[x][y]))
#Burada resmin tam orta noktasını bulmak için satır ve sütün sayılarını 2 ye bölüyoruz.
print("Resimin orta noktası = ",x,",",y)
#Resmin orta noktasını yazdırıyoruz.
print(img[0][0])
print(img[rows-1][cols-1])