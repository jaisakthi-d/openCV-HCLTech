import cv2
import numpy as np

img = cv2.imread("manufac_defect.png", cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)
good_count = 0
defect_count = 0
output = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
for i in range(1, num_labels): 
    x, y, w, h, area = stats[i]
    if area < 100:   
        defect_count += 1
        color = (0, 0, 255)  
    else:
        good_count += 1
        color = (0, 255, 0)  
    cv2.rectangle(output, (x, y), (x + w, y + h), color, 2)
print("Total solder joints:", num_labels - 1)
print("Good joints:", good_count)
print("Defective joints:", defect_count)
cv2.imshow("PCB Analysis", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
