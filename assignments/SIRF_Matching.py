import cv2

product_img = cv2.imread("product_img.webp")
logo_img = cv2.imread("logo_img.jpg")
product_gray = cv2.cvtColor(product_img, cv2.COLOR_BGR2GRAY)
logo_gray = cv2.cvtColor(logo_img, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(logo_gray, None)
kp2, des2 = sift.detectAndCompute(product_gray, None)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)
sift_result = cv2.drawMatches(logo_img, kp1, product_img, kp2, good_matches, None, flags=2)
cv2.imshow("SIFT Feature Matches", sift_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
