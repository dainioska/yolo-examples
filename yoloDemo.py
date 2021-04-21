# YOLO (cam) example from murtaza
import cv2 
import numpy as np 

cap = cv2.VideoCapture(1)
whT = 320
confThreshold = 0.5

classesFile = 'coco.names'
classNames = []
with open(classesFile, 'rt') as f:
    classNames =f.read().rstrip('\n').split('\n')
#print(classNames)

modelConfig = 'yolov3.cfg'
modelWeights = '/home/rodney/Downloads/yolov3.weights'
net = cv2.dnn.readNetFromDarknet(modelConfig, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

def findObjects(outputs, img):
    hT, wT, cT = img.shape
    bbox = []
    class_ids =[]
    confs = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            cofidence = scores[class_ids]
            if cofidence > confThreshold:
                w, h = det[2]*wT, det[3]*hT
                x, y = int((det[0]*wT) - w/2), int((det[0]*hT) - h/2)
                bbox.append(x, y, w, h)
                classIds.append(classId)
                confs.append (float(cofidence))
    print(len(bbox))


while True:
    success, img = cap.read()

    blob = cv2.dnn.blobFromImage(img, 1/255, (whT, whT), [0,0,0], 1, crop=False)
    net.setInput(blob)

    layerNames = net.getLayerNames()
    #print(layerNames)
    outputNames = [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]
    #print(outputNames)

    outputs = net.forward(outputNames)
    #print(outputs[0].shape)

    findObjects(outputs,img)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    
cv2.destroyAllWindows()