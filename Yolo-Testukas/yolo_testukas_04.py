# testing files from murtaza
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    img = cv2.resize(img, (640, 480))

    imgN = np.zeros((512,512,3), np.uint8)
    imgN[:] = [255, 255, 255]
    cv2.circle(imgN,(256, 256), 220,(0 ,0, 255), 2)
    cv2.line(imgN,(256,20),(256,500),(0,0,0),2)
    cv2.line(imgN,(20,256),(500,256),(0,0,0),2)
    
    cv2.imshow("Image",img)
    cv2.imshow("ImgN",imgN)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()