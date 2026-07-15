import cv2

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)

# Display original and blurred images
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred)

# Save blurred image
cv2.imwrite("blurred_image.jpg", blurred)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()