import cv2
import cv2.aruco as aruco
import numpy as np 
import os

def loadAugImages(path):
    myList = os.listdir(path)
    noOfMarkers =len(myList)
    print("Total Number of Markers Detected:", noOfMarkers)

def findArucoMarkers(img, markerSize=6, totalMarkers=250, draw=True):
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    # arucoDict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(imgGray, arucoDict, parameters=arucoParam)
    # print(ids)

    if draw:
        aruco.drawDetectedMarkers(img, bboxs)
    return [bboxs, ids]

def augmentAruco(bbox, id, img, imgAug, drawId=True):
    tl = bbox[0][0][0], bbox[0][0][1]
    tr = bbox[0][1][0], bbox[0][1][1]
    bl = bbox[0][2][0], bbox[0][2][1]
    br = bbox[0][3][0], bbox[0][3][1]

    h, w, c = imgAug.shape

    pts1 = np.array([tl, tr, br, bl])
    pts2 = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
    matrix, _ = cv2.findHomography(pts1, pts2)
    imgOut = cv2.warpPerspective(imgAug, matrix, (img.shape[1], img.shape[0]))
    cv2.fillConvexPoly(img, pts1.astype(int), (0, 0, 0))
    imgOut = img + imgOut

    if drawId:
        cv2.putText(imgOut, str(id), tl, cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 2)

    return imgOut

def main():
    cap = cv2.VideoCapture(0)
    imgAug = cv2.imread("Markers/pic1.png")
    loadAugImages("Markers")
    # imgAug = cv2.resize(imgAug, (240, 100))

    while True:
        _, img = cap.read()
        arucoFound = findArucoMarkers(img)
        
        # Loop through all the markers
        if len(arucoFound[0]) != 0:
            for bbox, id in zip(arucoFound[0], arucoFound[1]):
                #print(bbox,id)
                img = augmentAruco(bbox, id, img, imgAug)



        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()

