import cv2
import numpy as np

normal = cv2.imread("C:\\Users\\Asus\\Downloads\\archive (5)\\valid\\Ramipril 5 MG\\Ramipril 5 MG (1).jpg")
defective = cv2.imread("C:\\Users\\Asus\\Downloads\\archive (5)\\valid\\Ramipril 5 MG\\Ramipril 5 MG (2).jpg")
normal = cv2.resize(normal, (300,300))
defective = cv2.resize(defective, (300,300))
normal_gray = cv2.cvtColor(normal, cv2.COLOR_BGR2GRAY)
defective_gray = cv2.cvtColor(defective, cv2.COLOR_BGR2GRAY)
diff = cv2.absdiff(normal_gray, defective_gray)
cv2.imshow("Normal img", normal)
cv2.imshow("Defective img", defective)
cv2.imshow("Difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
