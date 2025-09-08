import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Asus\\Downloads\\archive (5)\\valid\\Ramipril 5 MG\\Ramipril 5 MG (3).jpg", cv2.IMREAD_GRAYSCALE)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
cv2.imshow("Original", img)
cv2.imshow("Laplacian", laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
