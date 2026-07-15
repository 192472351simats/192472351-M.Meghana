import cv2

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)

# Save the grayscale image
cv2.imwrite("grayscale_image.jpg", gray)

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()