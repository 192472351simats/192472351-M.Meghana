import cv2

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Cannot open image")
    exit()

# Select object using mouse
print("Select an object using the mouse.")
print("Press ENTER after selecting.")

roi = cv2.selectROI(
    "Select Object",
    image,
    showCrosshair=True,
    fromCenter=False
)

# Get coordinates
x, y, w, h = roi

# Check selection
if w == 0 or h == 0:
    print("No object selected")
    cv2.destroyAllWindows()
    exit()

# Draw rectangle
result = image.copy()

cv2.rectangle(
    result,
    (x, y),
    (x + w, y + h),
    (0, 255, 0),
    2
)

# Extract object
object_image = image[y:y+h, x:x+w]

# Display
cv2.imshow("Original with Rectangle", result)
cv2.imshow("Extracted Object", object_image)

# Save output
cv2.imwrite("rectangle_output.jpg", result)
cv2.imwrite("extracted_object.jpg", object_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Object extracted successfully.")