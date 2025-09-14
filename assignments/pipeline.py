import cv2
import numpy as np

img = cv2.imread("bottle.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 50, 150)
kernel = np.ones((3,3), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = img.copy()
for cnt in contours:
    if cv2.contourArea(cnt) > 50: 
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(output, (x,y), (x+w, y+h), (0,0,255), 2)

cv2.imshow("Original", img)
cv2.imshow("Edges", edges)
cv2.imshow("Defects Detected", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
