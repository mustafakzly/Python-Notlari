import cv2
import numpy as np
img = cv2.imread("resim1.jpg")
img = cv2.resize(img,(512,512))
print(img.shape)
rows,cols = img.shape[:2]

src_points = np.float32([
     [0,0],
     [cols-1,0],
     [0,rows-1],
     [cols-1,rows-1]])

dst_points = np.float32([
     [0,0],
     [cols-1,0],
     [int(0.33*(cols-1)),rows-1],
     [int(0.66*(cols-1)),rows-1]])

projective_matrix = cv2.getPerspectiveTransform(src_points,dst_points)
img_output = cv2.warpPerspective(img,projective_matrix,(cols,rows))

#belirli noktalardan fotoğrafı eğik yapma
# src_points = np.float32([
#     [0,0],
#     [cols-1,0],
#     [0,rows-1]])

# dst_points = np.float32([
#     [0,0],
#     [int(0.6*(cols-1)),0],
#     [int(0.4*(cols-1)),rows-1]])

# affine_matrix = cv2.getAffineTransform(src_points,dst_points)

# img_output = cv2.warpAffine(img,affine_matrix,(cols,rows))
# ------------------------------------------------------------------
#RESİMİ DÖNDÜRME
# rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),30,0.7)
# img_rotation = cv2.warpAffine(img,rotation_matrix,(cols,rows))
# ------------------------------------------------------------------
#RESİMİ BELLİ BİR PC KAYDIRMA
# translation_matrix = np.float32([
#     [1,0,25],
#     [0,1,25]])

# img_translation = cv2.warpAffine(img,translation_matrix,(cols+50,rows+50))    


#RESİMİ YENİDEN BOYUTLANDIRMA
# res = cv2.resize(img,(800,800))
# res = cv2.resize(img,None,fx=0.1,fy=0.1)

cv2.imshow("img",img)
cv2.imshow("img_output",img_output)
cv2.waitKey()
cv2.destroyAllWindows()