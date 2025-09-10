import cv2
import numpy as np
img = cv2.imread("C:\\Users\\Asus\\Downloads\\archive (5)\\valid\\Ramipril 5 MG\\Ramipril 5 MG (3).jpg", cv2.IMREAD_GRAYSCALE)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

magnitude = np.sqrt(sobelx**2 + sobely**2)
magnitude = np.uint8(magnitude)

cv2.imshow("Sobel X", np.uint8(np.absolute(sobelx)))
cv2.imshow("Sobel Y", np.uint8(np.absolute(sobely)))
cv2.imshow("Edge Magnitude", magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows() 