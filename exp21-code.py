import cv2
import numpy as np

# Load image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Laplacian mask with diagonal extension
kernel = np.array([
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]
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