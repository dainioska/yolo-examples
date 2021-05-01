"""
aruco picures testing example
"""
import cv2
import cv2.aruco as aruco
import numpy as np 
import os



def findArucoMarkers(img, markerSize=6, totalMarkers=250, draw=True):
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    # arucoDict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(imgGray, arucoDict, parameters=arucoParam)
    # print(bboxs)

    if draw:
        aruco.drawDetectedMarkers(img, bboxs)
    return [bboxs, ids]




def main():
    cap = cv2.VideoCapture(0)
    # imgAug = cv2.resize(imgAug, (240, 100))

    while True:
        _, img = cap.read()
        arucoFound = findArucoMarkers(img)
        
        # Loop through all the markers and augment each one
        if len(arucoFound[0]) != 0:
            for bbox, id in zip(arucoFound[0], arucoFound[1]):
                print(bbox, id)
                #img = augmentAruco(bbox, id, img, imgAug)



        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()

