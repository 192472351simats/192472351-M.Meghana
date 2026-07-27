import cv2
import numpy as np

# Read the image
image = cv2.imread("image.jpg")

# Check if the image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Get image dimensions
rows, cols = image.shape[:2]

# Translation values
tx = 100   # Move 100 pixels to the right
ty = 50    # Move 50 pixels downward

# Translation matrix
M = np.float32([[1, 0, tx],
                [0, 1, ty]])

# Apply translation
translated = cv2.warpAffine(image, M, (cols, rows))

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Translated Image", translated)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()