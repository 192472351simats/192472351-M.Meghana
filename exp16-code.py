import cv2

# Read input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Could not load input image.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to remove noise
blur = cv2.GaussianBlur(gray, (5, 5), 1.4)

# Perform Canny Edge Detection
edges = cv2.Canny(blur, threshold1=100, threshold2=200)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Canny Edge Detection", edges)

# Save output image
cv2.imwrite("canny_output.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()