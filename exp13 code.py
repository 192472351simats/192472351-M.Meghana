import cv2
import numpy as np

# Read the image
image = cv2.imread("image.jpg")

# Check if the image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

height, width = image.shape[:2]

# Define source points
src_pts = np.float32([
    [50, 50],
    [width - 50, 50],
    [50, height - 50],
    [width - 50, height - 50]
])

# Define destination points
dst_pts = np.float32([
    [0, 0],
    [width, 50],
    [50, height],
    [width - 50, height - 50]
])

# Compute Homography Matrix
H, status = cv2.findHomography(src_pts, dst_pts)

# Apply Homography Transformation
result = cv2.warpPerspective(image, H, (width, height))

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Homography Transformed Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()