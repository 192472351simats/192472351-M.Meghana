import cv2
import numpy as np

# Read image
img = cv2.imread("input.jpg")

if img is None:
    print("Error: Cannot open image")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Laplacian convolution kernel for boundary detection
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
], dtype=np.float32)

# Apply convolution
boundary = cv2.filter2D(gray, -1, kernel)

# Convert to absolute values
boundary = cv2.convertScaleAbs(boundary)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Boundary Image", boundary)

cv2.imwrite("boundary_output.jpg", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()