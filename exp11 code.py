import cv2
import numpy as np

# Read the image
image = cv2.imread("image.jpg")

# Check if the image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

rows, cols = image.shape[:2]

# Define three points in the original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Define corresponding points in the transformed image
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Compute the affine transformation matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply the affine transformation
transformed = cv2.warpAffine(image, M, (cols, rows))

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()