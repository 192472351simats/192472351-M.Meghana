import cv2
import numpy as np

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Create a kernel (3x3)
kernel = np.ones((3, 3), np.uint8)

# Dilate the image
dilated = cv2.dilate(image, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated)

# Save the output image
cv2.imwrite("dilated_image.jpg", dilated)

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()