import cv2

img = cv2.imread("input.jpg")

# Blur the image
blur = cv2.GaussianBlur(img, (5, 5), 0)

# High-boost filtering
A = 2.0
sharpened = cv2.addWeighted(img, A, blur, -(A - 1), 0)

# Save output
cv2.imwrite("high_boost.jpg", sharpened)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("High Boost Sharpened", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()