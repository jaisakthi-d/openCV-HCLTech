import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread("C:\\Users\\Asus\\Downloads\\archive (5)\\valid\\Ramipril 5 MG\\Ramipril 5 MG (1).jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale image:",gray)
plt.imshow(img)
plt.show()
#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV image",hsv)
#BGR to l*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)
#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)
cv.waitKey(0)