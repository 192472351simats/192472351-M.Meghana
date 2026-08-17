import cv2
import numpy as np

# Read image
img = cv2.imread("input.jpg")

if img is None:
    print("Error: Cannot open image")
    exit()

# Create structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Closing", closing)

cv2.imwrite("closing_output.jpg", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()