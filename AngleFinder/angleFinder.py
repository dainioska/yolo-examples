import cv2
import math

pointsList = []
img = cv2.imread('Samples/tumbnail.jpg')
img =cv2.resize(img, (640, 480))

def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
        pointsList.append([x, y])
        #print(pointsList)
        #print(x, y)

def gradient(pt1, pt2):
    return (pt2[1]-pt1[1]) / (pt2[0]-pt1[0])

def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    print(pt1, pt2, pt3)

while True:
    if len(pointsList) %3 == 0 and len(pointsList) != 0:
        getAngle()

    cv2.imshow("Image", img)
    cv2.setMouseCallback('Image' , mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList = []
        img = cv2.imread('Samples/tumbnail.jpg')
        img =cv2.resize(img, (640, 480))


