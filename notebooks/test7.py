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

img = thresh

color1 = (0, 255, 255)
color2 = (0, 255, 0)
color3 = (0, 0, 255)
color4 = (255, 0, 0)

# make question 1 boxes
q1_a = [
    [353, 25],
    [353, 46],
    [469, 46],
    [469, 25],
]
q1_b = [
    [235, 25],
    [235, 46],
    [351, 46],
    [351, 25],
]
q1_c = [
    [117, 25],
    [117, 46],
    [233, 46],
    [233, 25],
]
q1_d = [
    [0, 25],
    [0, 46],
    [115, 46],
    [115, 25],
]

# make question 2 boxes
q2_a = [
    [353, 71],
    [469, 71],
    [469, 92],
    [353, 92],
]
q2_b = [
    [235, 71],
    [235, 92],
    [351, 92],
    [351, 71],
]
q2_c = [
    [117, 71],
    [117, 92],
    [233, 92],
    [233, 71],
]
q2_d = [
    [0, 71],
    [0, 92],
    [115, 92],
    [115, 71],
]

# make question 3 boxes
q3_a = [
    [353, 190],
    [469, 190],
    [469, 210],
    [353, 210],
]
q3_b = [
    [235, 190],
    [351, 190],
    [351, 210],
    [235, 210],
]
q3_c = [
    [117, 190],
    [233, 190],
    [233, 210],
    [117, 210],
]
q3_d = [
    [0, 190],
    [115, 190],
    [115, 210],
    [0, 210],
]

# make question 4 boxes
q4_a = [
    [353, 236],
    [469, 236],
    [469, 257],
    [353, 257],
]
q4_b = [
    [235, 236],
    [351, 236],
    [351, 257],
    [235, 257],
]
q4_c = [
    [117, 236],
    [233, 236],
    [233, 257],
    [117, 257],
]
q4_d = [
    [0, 236],
    [115, 236],
    [115, 257],
    [0, 257],
]

# make question 5 boxes
q5_a = [
    [353, 283],
    [469, 283],
    [469, 304],
    [353, 304],
]
q5_b = [
    [235, 283],
    [351, 283],
    [351, 304],
    [235, 304],
]
q5_c = [
    [117, 283],
    [233, 283],
    [233, 304],
    [117, 304],
]
q5_d = [
    [0, 283],
    [115, 283],
    [115, 304],
    [0, 304],
]

# make question 6 boxes
q6_a = [
    [353, 330],
    [469, 330],
    [469, 352],
    [353, 352],
]
q6_b = [
    [235, 330],
    [351, 330],
    [351, 352],
    [235, 352],
]
q6_c = [
    [117, 330],
    [233, 330],
    [233, 352],
    [117, 352],
]
q6_d = [
    [0, 330],
    [115, 330],
    [115, 352],
    [0, 352],
]

# make question 7 boxes
q7_a = [
    [353, 376],
    [469, 376],
    [469, 398],
    [353, 398],
]
q7_b = [
    [235, 376],
    [351, 376],
    [351, 398],
    [235, 398],
]
q7_c = [
    [117, 376],
    [233, 376],
    [233, 398],
    [117, 398],
]
q7_d = [
    [0, 376],
    [115, 376],
    [115, 398],
    [0, 398],
]

# make question 8 boxes (3x height of other questions)
q8_a = [
    [353, 423],
    [469, 423],
    [469, 492],
    [353, 492],
]
q8_b = [
    [235, 423],
    [351, 423],
    [351, 492],
    [235, 492],
]
q8_c = [
    [117, 423],
    [233, 423],
    [233, 492],
    [117, 492],
]
q8_d = [
    [0, 423],
    [115, 423],
    [115, 492],
    [0, 492],
]

# make question 9 boxes
q9_a = [
    [353, 517],
    [469, 517],
    [469, 540],
    [353, 540],
]
q9_b = [
    [235, 517],
    [351, 517],
    [351, 540],
    [235, 540],
]
q9_c = [
    [117, 517],
    [233, 517],
    [233, 540],
    [117, 540],
]
q9_d = [
    [0, 517],
    [115, 517],
    [115, 540],
    [0, 540],
]

boxes = []
boxes.append([q1_a, q1_b, q1_c, q1_d])
boxes.append([q2_a, q2_b, q2_c, q2_d])
boxes.append([q3_a, q3_b, q3_c, q3_d])
boxes.append([q4_a, q4_b, q4_c, q4_d])
boxes.append([q5_a, q5_b, q5_c, q5_d])
boxes.append([q6_a, q6_b, q6_c, q6_d])
boxes.append([q7_a, q7_b, q7_c, q7_d])
boxes.append([q8_a, q8_b, q8_c, q8_d])
boxes.append([q9_a, q9_b, q9_c, q9_d])

contour_list = []
# draw contours for question 1
contour_list.append(cv2.drawContours(img, np.array([q1_a]), -1, color1, 1))
contour_list.append(cv2.drawContours(img, np.array([q1_b]), -1, color2, 1))
contour_list.append(cv2.drawContours(img, np.array([q1_c]), -1, color3, 1))
contour_list.append(cv2.drawContours(img, np.array([q1_d]), -1, color4, 1))

# draw contours for question 2
contour_list.append(cv2.drawContours(img, np.array([q2_a]), -1, color1, 1))
contour_list.append(cv2.drawContours(img, np.array([q2_b]), -1, color2, 1))
contour_list.append(cv2.drawContours(img, np.array([q2_c]), -1, color3, 1))
contour_list.append(cv2.drawContours(img, np.array([q2_d]), -1, color4, 1))

# draw contours for question 3
contour_list.append(cv2.drawContours(img, np.array([q3_a]), -1, color1, 1))
contour_list.append(cv2.drawContours(img, np.array([q3_b]), -1, color2, 1))
contour_list.append(cv2.drawContours(img, np.array([q3_c]), -1, color3, 1))
contour_list.append(cv2.drawContours(img, np.array([q3_d]), -1, color4, 1))

# draw contours for question 4
contour_list.append(cv2.drawContours(img, np.array([q4_a]), -1, color1, 1))
contour_list.append(cv2.drawContours(img, np.array([q4_b]), -1, color2, 1))
contour_list.append(cv2.drawContours(img, np.array([q4_c]), -1, color3, 1))
contour_list.append(cv2.drawContours(img, np.array([q4_d]), -1, color4, 1))

# draw contours for question 5
contour_list.append(cv2.drawContours(img, np.array([q5_a]), -1, color1, 1))
contour_list.append(cv2.drawContours(img, np.array([q5_b]), -1, color2, 1))
contour_list.append(cv2.drawContours(img, np.array([q5_c]), -1, color3, 1))
contour_list.append(cv2.drawContours(img, np.array([q5_d]), -1, color4, 1))

# draw contours for question 6
contour_list.append(cv2.drawContours(img, np.array([q6_a]), -1, color1, 1))
contour_list.append(cv2.drawContours(img, np.array([q6_b]), -1, color2, 1))
contour_list.append(cv2.drawContours(img, np.array([q6_c]), -1, color3, 1))
contour_list.append(cv2.drawContours(img, np.array([q6_d]), -1, color4, 1))

# draw contours for question 7
contour_list.append(cv2.drawContours(img, np.array([q7_a]), -1, color1, 1))
contour_list.append(cv2.drawContours(img, np.array([q7_b]), -1, color2, 1))
contour_list.append(cv2.drawContours(img, np.array([q7_c]), -1, color3, 1))
contour_list.append(cv2.drawContours(img, np.array([q7_d]), -1, color4, 1))

# draw contours for question 8
contour_list.append(cv2.drawContours(img, np.array([q8_a]), -1, color1, 1))
contour_list.append(cv2.drawContours(img, np.array([q8_b]), -1, color2, 1))
contour_list.append(cv2.drawContours(img, np.array([q8_c]), -1, color3, 1))
contour_list.append(cv2.drawContours(img, np.array([q8_d]), -1, color4, 1))

# draw contours for question 9
contour_list.append(cv2.drawContours(img, np.array([q9_a]), -1, color1, 1))
contour_list.append(cv2.drawContours(img, np.array([q9_b]), -1, color2, 1))
contour_list.append(cv2.drawContours(img, np.array([q9_c]), -1, color3, 1))
contour_list.append(cv2.drawContours(img, np.array([q9_d]), -1, color4, 1))

thresholds = []
for i in range(0, 9):
    thresholds_temp = []
    for j in range(0, 4):

        mask = np.zeros(thresh.shape, dtype="uint8")
        cv2.drawContours(mask, np.array([boxes[i][j]]), -1, 255, -1)

        mask = cv2.bitwise_and(thresh, thresh, mask=mask)
        total = cv2.countNonZero(mask)
        thresholds_temp.append(total)
    thresholds.append(thresholds_temp)

# showImage("test", img)
