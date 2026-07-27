import cv2
import numpy as np

# Read the image
image = cv2.imread("image.jpg")

# Check if the image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

rows, cols = image.shape[:2]

# Define four points in the original image
pts1 = np.float32([[50, 50],
                   [300, 50],
                   [50, 300],
                   [300, 300]])

# Define corresponding points in the output image
pts2 = np.float32([[0, 0],
                   [300, 0],
                   [100, 300],
                   [250, 300]])

# Compute the perspective transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the perspective transformation
transformed = cv2.warpPerspective(image, M, (cols, rows))

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()