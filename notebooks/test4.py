import cv2
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import imutils
from matplotlib import pyplot as plt
import random


def showImage(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)


def random_color():
    red = random.randint(10, 255)
    green = random.randint(10, 255)
    blue = random.randint(10, 255)

    # randomly zero out one of the colors
    color = random.randint(0, 2)
    if color == 0:
        red = 0
    elif color == 1:
        green = 0
    else:
        blue = 0
    print(red, green, blue)
    return (red, green, blue)


# Read the image:
test1_blank = cv2.imread("data/00-test1-blank.jpg")
gray = cv2.cvtColor(test1_blank, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)

# find contours in the edge map, then initialize
# the contour that corresponds to the document
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
docCnt = None
# ensure that at least one contour was found
if len(cnts) > 0:
    # sort the contours according to their size in
    # descending order
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    # loop over the sorted contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if our approximated contour has four points,
        # then we can assume we have found the paper
        if len(approx) == 4:
            docCnt = approx
            break

# apply a four point perspective transform to both the
# original image and grayscale image to obtain a top-down
# birds eye view of the paper
paper = four_point_transform(test1_blank, docCnt.reshape(4, 2))
warped = four_point_transform(gray, docCnt.reshape(4, 2))


# apply Otsu's thresholding method to binarize the warped
# piece of paper
thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

q1start1 = (469, 25)
q1end1 = (353, 46)

q1A = cv2.rectangle(thresh, q1start1, q1end1, (0, 255, 255))

q1start2 = (351, 25)
q1end2 = (235, 46)

q1B = cv2.rectangle(thresh, q1start2, q1end2, (255, 255, 255))

# construct a mask that reveals only the current
# "bubble" for the question
mask = np.zeros(thresh.shape, dtype="uint8")
cv2.drawContours(mask, [q1A], -1, 255, -1)
# apply the mask to the thresholded image, then
# count the number of non-zero pixels in the
# bubble area
mask = cv2.bitwise_and(thresh, thresh, mask=mask)
total = cv2.countNonZero(mask)
print(total)
showImage("thresh", thresh)
