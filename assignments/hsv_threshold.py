import cv2
import numpy as np
import glob

def classify_fruit(image_path):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_ripe = np.array([20, 100, 100])
    upper_ripe = np.array([35, 255, 255])
    mask = cv2.inRange(hsv, lower_ripe, upper_ripe)
    ripe_ratio = cv2.countNonZero(mask) / (img.shape[0] * img.shape[1])
    status = "Ripe" if ripe_ratio > 0.3 else "Unripe"
    print(f"{image_path}: {status}")
images = glob.glob("fruit_images/*.jpg")  
for img_path in images[:5]:
    classify_fruit(img_path)
