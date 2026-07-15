import cv2

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Rotate clockwise (90 degrees)
clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Rotate counter-clockwise (90 degrees)
counter_clockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter_clockwise)

# Save output images
cv2.imwrite("clockwise.jpg", clockwise)
cv2.imwrite("counter_clockwise.jpg", counter_clockwise)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()