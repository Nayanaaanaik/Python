import cv2

# Open the default camera (0)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the camera frame
    cv2.imshow("Webcam", frame)

    # Press ESC to exit
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()