"""
fece detection examples (mediapipe) from murtasa
"""
import cv2
import mediapipe as mp
import  time

cap =cv2.VideoCapture("Video/arm_01.mp4")
pTime = 0

while True:
    _, img = cap.read()

    # ---show FPS on image
    cTime =time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)


    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()