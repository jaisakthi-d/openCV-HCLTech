import cv2 as cv
#img=cv.imread('C:\\Users\\Asus\\OneDrive\\Desktop\\SecurityAppliance_SSL_CA(2)\Documents\\Pictures\\Screenshots\\Screenshot (128).png')
#cv.imshow('Photo',img)
#reading videos below
capture=cv.VideoCapture('C:\\Users\\Asus\\Videos\\Captures\\Cluster analysis using K-means,K-medoids algorithm using p - exe_9[1].pdf — Mozilla Firefox 2025-04-20 20-33-07.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0XFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)