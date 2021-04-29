# testing files from murtaza
import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    _, img = cap.read()
    print(img.shape)
    imgRes1 = cv2.resize(img, (500, 200))
    imgRes2 = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    #print(imgRes2.shape)
    imgCrop = img[100:200, 200:300]

    cv2.imshow("Image1",imgRes1)
    cv2.imshow("Image2",imgRes2)
    cv2.imshow("Crop", imgCrop)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()