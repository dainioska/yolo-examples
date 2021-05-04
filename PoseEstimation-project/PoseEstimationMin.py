"""
pose estimation examples (mediapipe) from murtasa
"""
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("../FaceDetection-project/Video/02.mp4")
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.55)

while True:
    _, img = cap.read()
    # img = cv2.resize(img, (640, 480))
    imRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # ---show FPS on image
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)


    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()