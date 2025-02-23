import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# Initialize hand detector
detector = HandDetector(maxHands=1)

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture image from webcam")
        break

    hands, img = detector.findHands(img)

    if hands:
        print("Hand detected")

    cv2.imshow("Image", img)

    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()