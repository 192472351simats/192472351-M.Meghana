import cv2
import numpy as np

# Read image
img = cv2.imread("input.jpg")

if img is None:
    print("Error: Cannot open image")
    exit()

# Create structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Erosion", erosion)

cv2.imwrite("erosion_output.jpg", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()