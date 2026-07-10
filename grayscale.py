import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("input.jpg")

# Check if the image was loaded
if img is None:
    print("Error: Could not find the image.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite("grayscale_output.jpg", gray)

# Display the grayscale image
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()
