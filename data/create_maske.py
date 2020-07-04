import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('20200508_140125_mask.png',0)
img[img<255]=0
cv2.imwrite('masks/mask.png', img)

