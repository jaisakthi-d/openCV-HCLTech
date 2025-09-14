import cv2 as cv
import numpy as np
img=cv.imread('C:\\Users\\Asus\\OneDrive\\Desktop\\SecurityAppliance_SSL_CA(2)\Documents\\Pictures\\Screenshots\\Screenshot (128).png')
cv.imshow("image",img)
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    print(transMat)
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
#-x->left,-y->up,x->right,y->down
translated=translate(img,300,100)
cv.imshow("Translated",translated)
#rotate an image
def rotate(img,angle,rotatePoint=None):
    (height,width)=img.shape[:2]
    if rotatePoint is None:
        rotatePoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotatePoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)
rotated_img=rotate(img,45)
cv.imshow("rotated image",rotated_img)
#Resizing
resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resized image",resize)
#flip an image
flip=cv.flip(img,0) #0-flips vertically,1-horizantally,-1 -both vertical and horizontally
cv.imshow("Flipped image",flip)
#cropping
cropped_img=img[100:200,300:400]
cv.waitKey(0)