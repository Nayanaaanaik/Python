import cv2

# ==========================
# Enter the full path of your video here
# ==========================
video_path = r"C:\Users\nayan\Downloads\Cars Moving On Road Stock Footage - Free Download.mp4"

# Open the video
cap = cv2.VideoCapture(video_path)

# Check if the video is opened successfully
if not cap.isOpened():
    print("Error: Cannot open the video.")
    exit()

print("Video is playing... Press 'q' to quit.")

# Read and display the video
while True:
    ret, frame = cap.read()

    # If there are no more frames, stop
    if not ret:
        print("Video has ended.")
        break

    # Display the video frame
    cv2.imshow("Road Video", frame)

    # Press 'q' on the keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
