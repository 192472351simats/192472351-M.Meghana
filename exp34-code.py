import cv2
import numpy as np

# Read image
img = cv2.imread("input.jpg")

if img is None:
    print("Error: Cannot open image")
    exit()

# Create structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply top hat transformation
top_hat = cv2.morphologyEx(
    img,
    cv2.MORPH_TOPHAT,
    kernel
)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Top Hat", top_hat)

cv2.imwrite("top_hat_output.jpg", top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()