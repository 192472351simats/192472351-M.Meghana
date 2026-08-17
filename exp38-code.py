import cv2

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Cannot open image")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles
for (x, y, w, h) in faces:

    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.putText(
        image,
        "Face",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

print("Number of faces detected:", len(faces))

cv2.imshow("Face Detection", image)
cv2.imwrite("face_detection_output.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()