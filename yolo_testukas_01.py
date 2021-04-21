# testing files from murtaza
import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    _, img = cap.read()
    img = cv2.resize(img, (640, 480))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3, 3), 0)
    imgCanny = cv2.Canny(imgBlur,100, 150)
    kernel =np.ones((5,5), np.uint8)
    imgDil = cv2.dilate(imgCanny,kernel,iterations=2)
    imgErode = cv2.erode(imgDil, kernel, iterations=1)


    #cv2.imshow("Image",img)
    #cv2.imshow("Gray",imgGray)
    #cv2.imshow("Blur",imgBlur)
    cv2.imshow("Canny",imgCanny)
    cv2.imshow("Dilation",imgDil)
    cv2.imshow("Erode",imgErode)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()