import cv2
import numpy as np

# Read image
img = cv2.imread("input.jpg")

if img is None:
    print("Error: Cannot open image")
    exit()

# Create structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply black hat transformation
black_hat = cv2.morphologyEx(
    img,
    cv2.MORPH_BLACKHAT,
    kernel
)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Black Hat", black_hat)

cv2.imwrite("black_hat_output.jpg", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()