import cv2
import numpy as np

img = cv2.imread("manufac_defect.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 50, 150)
kernel = np.ones((3,3), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)
eroded = cv2.erode(dilated, kernel, iterations=1)
contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = img.copy()
for cnt in contours:
    if cv2.contourArea(cnt) > 50:  
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(output, (x,y), (x+w, y+h), (0,0,255), 2)
        cv2.putText(output, "Defect", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

cv2.imshow("Original PCB", img)
cv2.imshow("Edges", edges)
cv2.imshow("Defects Detected", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
