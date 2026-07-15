import cv2
import numpy as np

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Create a 3x3 kernel
kernel = np.ones((3, 3), np.uint8)

# Erode the image
eroded = cv2.erode(image, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded)

# Save the output image
cv2.imwrite("eroded_image.jpg", eroded)

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()