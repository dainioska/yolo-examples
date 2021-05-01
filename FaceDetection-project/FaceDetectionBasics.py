"""
fece detection examples (mediapipe) from murtasa
"""
import cv2
import mediapipe as mp
import  time

cap =cv2.VideoCapture("Video/arm_01.mp4")

while True:
    _, img = cap.read()


    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()