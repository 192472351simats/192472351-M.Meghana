import cv2

img = cv2.imread("input.jpg")

# Watermark text
text = "MY WATERMARK"

# Position
x = 20
y = img.shape[0] - 30

# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 255, 255)
thickness = 2

# Add watermark
cv2.putText(
    img,
    text,
    (x, y),
    font,
    font_scale,
    color,
    thickness,
    cv2.LINE_AA
)

# Save output
cv2.imwrite("watermarked.jpg", img)

# Display
cv2.imshow("Watermarked Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()