import cv2

# Read input image
image = cv2.imread("input.jpg")

# Read watch template
template = cv2.imread("watch_template.jpg")

if image is None or template is None:
    print("Error: Cannot open image or template")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Get template dimensions
h, w = gray_template.shape

# Template matching
result = cv2.matchTemplate(
    gray_image,
    gray_template,
    cv2.TM_CCOEFF_NORMED
)

# Find best match
_, max_value, _, max_location = cv2.minMaxLoc(result)

# Set threshold
threshold = 0.6

if max_value >= threshold:
    x, y = max_location

    # Draw rectangle around detected watch
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.putText(
        image,
        "Watch Detected",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    print("Watch detected")
else:
    print("Watch not detected")

cv2.imshow("Watch Recognition", image)
cv2.imwrite("watch_result.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()