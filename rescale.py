import cv2 as cv

img = cv.imread('images/cat_large.jpg')


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    # print(dimensions, type(dimensions))

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_img = rescaleFrame(img, 0.25)

cv.imshow('Cat Large', resized_img)

cv.waitKey(0)