import cv2 as cv
img=cv.imread('C:\\Users\\Asus\\OneDrive\\Desktop\\SecurityAppliance_SSL_CA(2)\Documents\\Pictures\\Screenshots\\Screenshot (128).png')
def resize(frame,scale=0.25):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
resized_img=resize(img)
cv.imshow('Image resized',resized_img)
cv.waitKey(0)