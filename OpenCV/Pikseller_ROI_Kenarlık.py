import cv2
import matplotlib.pyplot as plt
resim = cv2.imread("limon.jpg")


kirp = resim[500:800,500:800]

resim[150:450,1200:1500] = kirp

plt.subplot(121)
plt.imshow(resim)
plt.subplot(122)
plt.imshow(kirp)
plt.show()