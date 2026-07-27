import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access the webcam.")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20.0

out = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

print("Press 'q' to stop recording.")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    out.write(frame)
    cv2.imshow("Webcam Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video captured and saved as output.mp4")