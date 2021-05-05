"""
angle trainer example from murtasa
testing
"""

import cv2
import numpy as np
import PoseModule as pm

cap = cv2.VideoCapture("../Samples/arm_01.mp4")
detector = pm.poseDetector()

while True:
    _, img = cap.read()
    img = cv2.resize(img, (640, 480))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Image",img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()