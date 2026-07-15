import cv2

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Scale image to a bigger size (2x)
bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# Scale image to a smaller size (0.5x)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

# Save output images
cv2.imwrite("bigger_image.jpg", bigger)
cv2.imwrite("smaller_image.jpg", smaller)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()