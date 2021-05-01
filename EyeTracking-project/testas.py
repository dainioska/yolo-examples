import cv2


img = cv2.imread('/home/rodney/Desktop/GIT_py/yolo-examples/Yolo-Testukas/Resources/lena.png')

cv2.imshow("Image", img)
cv2.waitKey(0)