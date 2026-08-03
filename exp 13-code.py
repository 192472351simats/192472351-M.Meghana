import cv2
import numpy as np

# Open the input video
cap = cv2.VideoCapture("input_video.mp4")

# Check whether the video is opened
if not cap.isOpened():
    print("Error: Cannot open the video.")
    exit()

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    "perspective_output.mp4",
    fourcc,
    fps,
    (width, height)
)

# Define source points
src_points = np.float32([
    [100, 100],
    [width - 100, 100],
    [100, height - 100],
    [width - 100, height - 100]
])

# Define destination points
dst_points = np.float32([
    [0, 0],
    [width - 1, 0],
    [0, height - 1],
    [width - 1, height - 1]
])

# Calculate perspective transformation matrix
matrix = cv2.getPerspectiveTransform(
    src_points,
    dst_points
)

while True:

    # Read one frame
    success, frame = cap.read()

    # Stop when the video ends
    if not success:
        break

    # Apply perspective transformation
    transformed_frame = cv2.warpPerspective(
        frame,
        matrix,
        (width, height)
    )

    # Display original video
    cv2.imshow(
        "Original Video",
        frame
    )

    # Display transformed video
    cv2.imshow(
        "Perspective Transformed Video",
        transformed_frame
    )

    # Save transformed frame
    out.write(transformed_frame)

    # Press Q to stop
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Release video objects
cap.release()
out.release()

# Close all windows
cv2.destroyAllWindows()

print("Perspective transformation completed!")
print("Output saved as perspective_output.mp4")