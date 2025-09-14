import cv2 as cv
import numpy as np
img=cv.imread('C:\\Users\\Asus\\OneDrive\\Desktop\\SecurityAppliance_SSL_CA(2)\Documents\\Pictures\\Screenshots\\Screenshot (128).png')
blank=np.zeros((500,500,3),dtype='uint8') 
#painting image in certain colour
blank[200:300,300:400]=0,0,0
#cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=-1)
#Drawing a circle
#cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),2,(255,0,0),thickness=-1)
#Draw a line   
cv.line(blank,(100,250),(300,400),(255,111,128),thickness=2)
#Writing a text on an image
#cv.putText(blank,'Hello world!',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),thickness=2)
cv.imshow('Image',blank)
cv.waitKey(0)