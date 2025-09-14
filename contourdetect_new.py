import cv2 as cv
import numpy as np
img = cv.imread("C:\\Users\\Asus\\Downloads\\archive (5)\\valid\\Ramipril 5 MG\\Ramipril 5 MG (3).jpg", cv.IMREAD_GRAYSCALE)
blank=np.zeros(img.shape,dtype='uint8')
#blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
canny=cv.Canny(img,130,170)
cv.imshow("canny edge detector",canny)
#_,thresh=cv.threshold(img,125,255,cv.THRESH_BINARY)
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f"contours found :{len(contours)}")
cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow("Contours drawn",blank)
cv.waitKey(0)