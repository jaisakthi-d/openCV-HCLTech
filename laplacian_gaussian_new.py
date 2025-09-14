import cv2
import numpy as np
img = cv2.imread("C:\\Users\\Asus\\Downloads\\archive (5)\\valid\\apixaban 2.5 MG\\apixaban 2.5 MG (7) - Copy - Copy.jpg", cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(img, (3,3), 0)
edges = cv2.Laplacian(blurred, cv2.CV_64F)
laplacian = np.uint8(np.absolute(edges))
_, thresh = cv2.threshold(laplacian, 30, 255, cv2.THRESH_BINARY)
cv2.imshow("Original", img)
cv2.imshow("Gaussian Blurred", blurred)
cv2.imshow("Laplacian", laplacian)
cv2.imshow("Thresholded Defects", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
