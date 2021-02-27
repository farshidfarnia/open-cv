import cv2
import numpy as np

img = cv2.imread('Resources/lambo.png')
print(img.shape)
imgResize = cv2.resize(img, (600, 200))
print(imgResize.shape)
imgCropped = img[0:200, 200:500]

cv2.imshow('Original Image', img)
cv2.imshow('Resize Image', imgResize)
cv2.imshow('Image Cropped', imgCropped)
cv2.waitKey(0)
