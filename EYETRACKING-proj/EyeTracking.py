import cv2
import numpy as np
import SerialModule as sm
import ObjectDetectionModule as odm
import time

frameW = 640
frameH = 480
path1 ='/home/rodney/Desktop/GIT_py/yolo-examples/EYETRACKING-proj/haarcascade_frontalface_default.xml'

cap = cv2.VideoCapture(1)
faceCascade = cv2.CascadeClassifier(path1)

def findCenter(imgObjects, objects):
    cx, cy = -1, -1
    if len(objects) != 0:
        x, y, w, h = objects[0][0]
        cx = x + w//2
        cy = y + h//2
        print(cx)
        cv2.circle(imgObjects,(cx, cy), 2, (0, 255, 0), cv2.FILLED)
        ih, iw, ic = imgObjects.shape
        cv2.line(imgObjects, (iw//2, cy), (cx, cy), (0, 255, 0), 1)
        cv2.line(imgObjects, (cx, ih//2), (cx, cy), (0, 255, 0), 1)
    return cx, cy, imgObjects


while True:
    _, img = cap.read()
    img = cv2.resize(img, (0, 0), None, 0.3, 0.3)
    imgObjects, objects = odm.findObjects(img, faceCascade, 1.08, 10)
    cx, cy, imgObjects = findCenter(imgObjects, objects)

    h, w, c = imgObjects.shape
    cv2.line(imgObjects, (w//2, 0), (w//2, h), (255, 0, 255), 1)
    cv2.line(imgObjects, (0, h//2), (w, h//2), (255, 0, 255), 1)
    
    img = cv2.resize(imgObjects, (0,0), None, 3, 3)
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        sm.sendData(ser,[90,90],3)
        break

cv2.destroyAllWindows()