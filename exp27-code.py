import cv2

# Read images
source = cv2.imread("input.jpg")
destination = cv2.imread("destination.jpg")

# Crop a portion from source image
crop = source[50:250, 50:250]

# Resize cropped image
crop = cv2.resize(crop, (200, 200))

# Position where crop will be pasted
x = 100
y = 100

# Copy and paste
destination[y:y+200, x:x+200] = crop

# Save output
cv2.imwrite("copy_paste.jpg", destination)

# Display
cv2.imshow("Source Image", source)
cv2.imshow("Cropped Image", crop)
cv2.imshow("Copy Paste Result", destination)

cv2.waitKey(0)
cv2.destroyAllWindows()