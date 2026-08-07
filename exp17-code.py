import cv2
import numpy as np

# Read input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Could not load input image.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Sobel Edge Detection along X-axis
sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)

# Convert result to absolute values for display
sobel_x = cv2.convertScaleAbs(sobel_x)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Sobel X Edge Detection", sobel_x)

# Save output image
cv2.imwrite("sobel_x_output.jpg", sobel_x)

cv2.waitKey(0)
cv2.destroyAllWindows()