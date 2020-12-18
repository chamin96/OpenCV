import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. paint the image with a color
# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Red', blank)

# 2. draw a rectangle
cv.rectangle(blank, (0,0), (250,500), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# 4. draw a line
cv.line(blank, (0,0), (250,250), (255,255,255), thickness=4)
cv.imshow('Line', blank)

# 5. write text
img = cv.imread('images/girl.jpg')
cv.putText(img, 'Hello', (255,150), cv.FONT_HERSHEY_TRIPLEX, 1.0, (150,150,255), thickness=2)
cv.imshow('Girl', img)

cv.waitKey(0)