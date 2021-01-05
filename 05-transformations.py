import cv2 as cv
import numpy as np

img = cv.imread("images/boy.jpg")

cv.imshow("Boy", img)

# translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])   # translation matrix
    dimensions = (img.shape[1], img.shape[0])       # width, height of the image
    return cv.warpAffine(img, transMat, dimensions)

# -y --> Up
# -x --> Left
# y --> Down
# x --> Right

translated = translate(img, 100, 100)       # shifting image right and down by 100 pixels
cv.imshow("Translated", translated)

cv.waitKey(0)