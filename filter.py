import cv2
import numpy as np

img = cv2.imread("automotive.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
laplacian_bgr = cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR)
img_new = np.hstack((img, laplacian_bgr))
cv2.imshow("Original and Laplacian", img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
