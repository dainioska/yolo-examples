# VIDEO test code
# import cv2

# frameW = 640
# frameH = 480
# cap = cv2.VideoCapture('../Samples/road_01.mp4')

# while True:
#     _, img = cap.read()
#     img = cv2.resize(img, (frameW, frameH))
#     cv2.imshow("Image",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# CAM test code
import cv2

frameW = 640
frameH = 480
cap = cv2.VideoCapture(1)

while True:
    _, img = cap.read()
    img = cv2.resize(img, (frameW, frameH))
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()