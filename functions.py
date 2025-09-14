import cv2 as cv
img=cv.imread('C:\\Users\\Asus\\OneDrive\\Desktop\\SecurityAppliance_SSL_CA(2)\Documents\\Pictures\\Screenshots\\Screenshot (128).png')\
#Converting an image to grayscale
gscale=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#blur an image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("image",blur)
#Edge cascade-to find edges in an image
canny=cv.Canny(blur,125,175)
#Diluting the image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow("image",dilated)
#erode an image
eroded=cv.erode(dilated,(7,7),iterations=3)
#resize image
resized_img=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
#cropping an image
cropped_img=img[50:200,200:400]
cv.imshow("image",cropped_img)
cv.waitKey(0)