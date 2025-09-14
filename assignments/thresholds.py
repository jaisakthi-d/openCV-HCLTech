import cv2
import numpy as np

img = cv2.imread("metal_img.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original",img)
_, global_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
adaptive_mean = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
_, otsu_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
combined = np.hstack((global_thresh, adaptive_mean, otsu_thresh))
cv2.imshow("Global  Adaptive  Otsu", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
