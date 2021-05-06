"""
mediapipe pose example from nicolas renote
2021-05-06 testing
"""
import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret, frame = cap.read()
    # frame = cv2.resize(img, (640, 480))
    cv2.imshow("MPfeed", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()