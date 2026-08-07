import cv2
import numpy as np

# Read the input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
h, w = image.shape[:2]

# Define source points (corners of the original image)
src_points = np.float32([
    [0, 0],
    [w - 1, 0],
    [w - 1, h - 1],
    [0, h - 1]
])

# Define destination points (change these for perspective effect)
dst_points = np.float32([
    [50, 50],
    [w - 100, 20],
    [w - 50, h - 50],
    [100, h - 20]
])

# Compute Homography Matrix
H, status = cv2.findHomography(src_points, dst_points)

print("Homography Matrix:")
print(H)

# Apply Perspective Transformation
output = cv2.warpPerspective(image, H, (w, h))

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Transformed Image", output)

# Save output image
cv2.imwrite("output.jpg", output)

cv2.waitKey(0)
cv2.destroyAllWindows()