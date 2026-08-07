import cv2
import numpy as np

# Load image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Laplacian mask with positive center coefficient
kernel = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
], dtype=np.float32)

# Apply filter
laplacian = cv2.filter2D(img, cv2.CV_32F, kernel)
laplacian = cv2.convertScaleAbs(laplacian)

# Sharpen image
sharpened = cv2.add(img, laplacian)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Laplacian", laplacian)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()