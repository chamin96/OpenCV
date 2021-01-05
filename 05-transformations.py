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

# rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    print(height, width)

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -90)
cv.imshow("Rotated", rotated)


# Resizing

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)


cv.waitKey(0)