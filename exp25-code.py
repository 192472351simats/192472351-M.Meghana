import cv2
import numpy as np

img = cv2.imread("input.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate gradients using Sobel
gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Calculate gradient magnitude
gradient = cv2.magnitude(
    gx.astype(np.float32),
    gy.astype(np.float32)
)

# Normalize gradient
gradient = cv2.normalize(
    gradient, None, 0, 255, cv2.NORM_MINMAX
).astype(np.uint8)

# Create gradient mask
mask = gradient.astype(np.float32) / 255.0

# Laplacian for sharpening
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Apply gradient mask
sharpened = img.astype(np.float64) - (
    laplacian * mask[:, :, np.newaxis]
)

# Convert to uint8
sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)

# Save output
cv2.imwrite("gradient_sharpened.jpg", sharpened)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Gradient Mask", gradient)
cv2.imshow("Gradient Sharpened", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()