import cv2 as cv
img=cv.imread("C:\\Users\\Asus\\Downloads\\archive (5)\\train\\montelukast 10 MG\\montelukast 10 MG (1) - Copy.jpg")
cv.imshow("Normal image",img)
#Averaging
#higher the kernel size highers blur effect
avg=cv.blur(img,(3,3))
cv.imshow("Average blurring",avg)
#Gaussian blurring
gauss=cv.GaussianBlur(img,(5,5),0)
cv.imshow("Gaussian blur",gauss)
#median blur
median=cv.medianBlur(img,3)
cv.imshow("Median blur",median)
#bilateral blurring
bilateral=cv.bilateralFilter(img,5,15,15)
cv.imshow("Bilateral",bilateral)
cv.waitKey(0)
