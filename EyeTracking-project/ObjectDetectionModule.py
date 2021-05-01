"""
Object detection module MODIFIED
"""
import cv2

path1 = ('/home/rodney/Desktop/GIT_py/yolo-examples/Yolo-Testukas/Resources/lena.png')
path2 = ('/home/rodney/Desktop/GIT_py/yolo-examples/Yolo-Testukas/Resources/haarcascade_frontalface_default.xml')

def findObjects(img, objectCascade, scaleF=1.1, minN =4):
    """
       finds objects using haarcascade file
       :param img: Image in which the objects need to find
       :param objectCascade: Object Cascade created with Cascade Classifier
       :param scaleF: how much the image sizes reduced at each image scale
       :param minN: how many neighbours each rectangle should have to accept as valid
       :return: image with rectangles draw and the bounding bow info
    """
    imgObjects = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objects = objectCascade.detectMultiScale(imgGray, scaleF, minN)
    objectsOut = []
    for (x, y, w, h) in objects:
        cv2.rectangle(imgObjects, (x, y), (x+w, y+h), (255, 0, 255), 2)
        objectsOut.append([[x, y, w, h],[w+h]])

    objectsOut = sorted(objectsOut, key=lambda x:x[1], reverse=True)

    return imgObjects, objectsOut

def main():
    img = cv2.imread(path1)
    faceCascade = cv2.CascadeClassifier(path2)
    imgObjects, objects = findObjects(img, faceCascade)
    cv2.imshow("Output", imgObjects)
    cv2.waitKey(0)


if __name__ == "__main__":
     main()