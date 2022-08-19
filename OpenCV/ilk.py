import cv2
from matplotlib import pyplot as plt
resim = cv2.imread("resim1.jpg")


cv2.namedWindow("resim",cv2.WINDOW_NORMAL)
cv2.imshow("resim",resim)
#window_autosize orjinal boyutunda verir
#window_normal küçültüp büyültünce ekranı kaplar
#0 yazarsak resim gri tonlamalarına dönüşür
cv2.imshow("resim penceresi",resim)
plt.imshow(resim, cmap="gray")
plt.show()
k = cv2.waitKey(0)

if k == 27:
    print("ESC  tuşuna basıldı.")
elif k == ord("q"):
    print("q tuşuna basıldı, resim kayıt edildi")
    cv2.imwrite("resim1gri.jpg",resim)
#cv2.destroyWindows("resim penceresi")
cv2.destroyAllWindows("resim penceresi")