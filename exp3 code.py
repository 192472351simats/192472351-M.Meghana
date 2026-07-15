import cv2

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using Canny
edges = cv2.Canny(blur, 100, 200)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Canny Edge Detection", edges)

# Save the output image
cv2.imwrite("canny_output.jpg", edges)

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()