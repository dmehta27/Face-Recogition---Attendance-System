import cv2
import numpy as np

def gamma_correction(img, correction):
    img = img/255.0
    img = cv2.pow(img, correction)
    return np.uint8(img*255)

img = cv2.imread('zz.jpg', 0) #gray image
dst = gamma_correction(img, 0.5)
cv2.imshow("gamme",dst)
