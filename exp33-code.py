import cv2
import numpy as np

# Read image
img = cv2.imread("input.jpg")

if img is None:
    print("Error: Cannot open image")
    exit()

# Create structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply morphological gradient
gradient = cv2.morphologyEx(
    img,
    cv2.MORPH_GRADIENT,
    kernel
)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Morphological Gradient", gradient)

cv2.imwrite("gradient_output.jpg", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()