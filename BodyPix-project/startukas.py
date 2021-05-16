import cv2
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
from tf_bodypix.api import  download_model, load_model, BodyPixModelPaths

bodypix_model = load_model(download_model(BodyPixModelPaths.MOBILENET_FLOAT_50_STRIDE_16))

img = cv2.imread("../Samples/tumbnail.jpg")
img = cv2.resize(img, (640, 480))
print(img.shape)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    # BodyPix detection
    result = bodypix_model.predict_single(frame)
    mask = result.get_mask(threshold=0.5).numpy().astype(np.uint8)
    masked_image = cv2.bitwise_and(frame, frame,mask=mask)

    # Apply virtual background
    neg = np.add(mask, -1)
    inverse = np.where(neg == -1, 1, neg).astype(np.uint8)
    masked_background = cv2.bitwise_and(img, img, mask=inverse)
    final = cv2.add(masked_image, masked_background)

    cv2.imshow("BodyPix", masked_image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()