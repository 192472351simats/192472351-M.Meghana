import cv2
import numpy as np

# Read input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Could not load input image.")
    exit()

height, width = image.shape[:2]

# Source points (corners of the image)
src_pts = np.array([
    [0, 0],
    [width - 1, 0],
    [width - 1, height - 1],
    [0, height - 1]
], dtype=np.float32)

# Destination points (change these for different transformations)
dst_pts = np.array([
    [50, 50],
    [width - 80, 30],
    [width - 30, height - 50],
    [80, height - 20]
], dtype=np.float32)

# Compute Homography using Direct Linear Transformation (DLT)
H, mask = cv2.findHomography(src_pts, dst_pts, method=0)

print("Homography Matrix (DLT):")
print(H)

# Apply perspective transformation
transformed = cv2.warpPerspective(image, H, (width, height))

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("DLT Transformed Image", transformed)

# Save output
cv2.imwrite("dlt_output.jpg", transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()