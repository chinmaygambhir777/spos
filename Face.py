from deepface import DeepFace
import cv2

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Analyze emotions
    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

    # Extract dominant emotion
    emotion = result[0]['dominant_emotion']

    # Display result
    cv2.putText(frame, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("Emotion Recognition", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
