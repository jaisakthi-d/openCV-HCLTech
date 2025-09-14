import cv2
import numpy as np

img = cv2.imread("tablet_img.webp")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
if np.sum(binary == 255) > np.sum(binary == 0):
    binary = cv2.bitwise_not(binary)
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)
print("Number of connected components (including background):", num_labels)
output = img.copy()
for i in range(1, num_labels):
    x, y, w, h, area = stats[i]
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if area < 100 or area > 2000:
        label = "Defect"
        color = (0, 0, 255) 
    else:
        label = "OK"
        color = (0, 255, 0)  

    cv2.putText(output, f"{label}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    print(f"Component {i}: Area={area}, Status={label}")

cv2.imshow("Binary", binary)
cv2.imshow("Detected Tablets", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
