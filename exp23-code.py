import cv2

# Load image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Gaussian blur
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Unsharp masking
sharpened = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()