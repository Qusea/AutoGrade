import cv2
import numpy as np

img = cv2.imread("data/00-test1-blank-paper.jpg")


def showImage(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)


color1 = (0, 255, 255)
color2 = (0, 255, 0)
color3 = (0, 0, 255)
color4 = (255, 0, 0)

# make question 1 boxes
q1 = [[[353, 25], [353, 46], [469, 46], [469, 25],],[[235, 25], [235, 46], [351, 46], [351, 25],],[[117, 25], [117, 46], [233, 46], [233, 25],],[[0, 25], [0, 46], [115, 46], [115, 25],]]

# make question 2 boxes
q2 = [[[353, 71], [469, 71], [469, 92], [353, 92],],[[235, 71], [235, 92], [351, 92], [351, 71],],[[117, 71], [117, 92], [233, 92], [233, 71],],[[0, 71], [0, 92], [115, 92], [115, 71],]]

# make question 3 boxes
q3 = [[[353, 190], [469, 190], [469, 210], [353, 210],],[[235, 190], [351, 190], [351, 210], [235, 210],],[[117, 190], [233, 190], [233, 210], [117, 210],],[[0, 190], [115, 190], [115, 210], [0, 210],]]

# make question 4 boxes
q4 = [[[353, 236], [469, 236], [469, 257], [353, 257],],[[235, 236], [351, 236], [351, 257], [235, 257],],[[117, 236], [233, 236], [233, 257], [117, 257],],[[0, 236], [115, 236], [115, 257], [0, 257],]]

# make question 5 boxes
q5 = [[[353, 283], [469, 283], [469, 304], [353, 304],],[[235, 283], [351, 283], [351, 304], [235, 304],],[[117, 283], [233, 283], [233, 304], [117, 304],],[[0, 283], [115, 283], [115, 304], [0, 304],]]

# make question 6 boxes
q6 = [[[353, 330], [469, 330], [469, 352], [353, 352],],[[235, 330], [351, 330], [351, 352], [235, 352],],[[117, 330], [233, 330], [233, 352], [117, 352],],[[0, 330], [115, 330], [115, 352], [0, 352],]]

# make question 7 boxes
q7 = [[[353, 376], [469, 376], [469, 398], [353, 398],],[[235, 376], [351, 376], [351, 398], [235, 398],],[[117, 376], [233, 376], [233, 398], [117, 398],],[[0, 376], [115, 376], [115, 398], [0, 398],]]

# make question 8 boxes (3x height of other questions)
q8_a = [[353, 423], [469, 423], [469, 492], [353, 492],]
q8_b = [[235, 423], [351, 423], [351, 492], [235, 492],]
q8_c = [[117, 423], [233, 423], [233, 492], [117, 492],]
q8_d = [[0, 423], [115, 423], [115, 492], [0, 492],]

# make question 9 boxes
q9_a = [[353, 517], [469, 517], [469, 540], [353, 540],]
q9_b = [[235, 517], [351, 517], [351, 540], [235, 540],]
q9_c = [[117, 517], [233, 517], [233, 540], [117, 540],]
q9_d = [[0, 517], [115, 517], [115, 540], [0, 540],]

contours = []
# draw contours for question 1
contours.append(cv2.drawContours(img, np.array(q1), -1, color1, 1))
# contours.append(cv2.drawContours(img, np.array([q1_b]), -1, color2, 1))
# contours.append(cv2.drawContours(img, np.array([q1_c]), -1, color3, 1))
# contours.append(cv2.drawContours(img, np.array([q1_d]), -1, color4, 1))

# draw contours for question 2
contours.append(cv2.drawContours(img, np.array(q2), -1, color1, 1))
# contours.append(cv2.drawContours(img, np.array([q2_b]), -1, color2, 1))
# contours.append(cv2.drawContours(img, np.array([q2_c]), -1, color3, 1))
# contours.append(cv2.drawContours(img, np.array([q2_d]), -1, color4, 1))

# draw contours for question 3
contours.append(cv2.drawContours(img, np.array(q3), -1, color1, 1))
# contours.append(cv2.drawContours(img, np.array([q3_b]), -1, color2, 1))
# contours.append(cv2.drawContours(img, np.array([q3_c]), -1, color3, 1))
# contours.append(cv2.drawContours(img, np.array([q3_d]), -1, color4, 1))

# draw contours for question 4
contours.append(cv2.drawContours(img, np.array([q4_a]), -1, color1, 1))
contours.append(cv2.drawContours(img, np.array([q4_b]), -1, color2, 1))
contours.append(cv2.drawContours(img, np.array([q4_c]), -1, color3, 1))
contours.append(cv2.drawContours(img, np.array([q4_d]), -1, color4, 1))

# draw contours for question 5
contours.append(cv2.drawContours(img, np.array([q5_a]), -1, color1, 1))
contours.append(cv2.drawContours(img, np.array([q5_b]), -1, color2, 1))
contours.append(cv2.drawContours(img, np.array([q5_c]), -1, color3, 1))
contours.append(cv2.drawContours(img, np.array([q5_d]), -1, color4, 1))

# draw contours for question 6
contours.append(cv2.drawContours(img, np.array([q6_a]), -1, color1, 1))
contours.append(cv2.drawContours(img, np.array([q6_b]), -1, color2, 1))
contours.append(cv2.drawContours(img, np.array([q6_c]), -1, color3, 1))
contours.append(cv2.drawContours(img, np.array([q6_d]), -1, color4, 1))

# draw contours for question 7
contours.append(cv2.drawContours(img, np.array([q7_a]), -1, color1, 1))
contours.append(cv2.drawContours(img, np.array([q7_b]), -1, color2, 1))
contours.append(cv2.drawContours(img, np.array([q7_c]), -1, color3, 1))
contours.append(cv2.drawContours(img, np.array([q7_d]), -1, color4, 1))

# draw contours for question 8
contours.append(cv2.drawContours(img, np.array([q8_a]), -1, color1, 1))
contours.append(cv2.drawContours(img, np.array([q8_b]), -1, color2, 1))
contours.append(cv2.drawContours(img, np.array([q8_c]), -1, color3, 1))
contours.append(cv2.drawContours(img, np.array([q8_d]), -1, color4, 1))

# draw contours for question 9
contours.append(cv2.drawContours(img, np.array([q9_a]), -1, color1, 1))
contours.append(cv2.drawContours(img, np.array([q9_b]), -1, color2, 1))
contours.append(cv2.drawContours(img, np.array([q9_c]), -1, color3, 1))
contours.append(cv2.drawContours(img, np.array([q9_d]), -1, color4, 1))

showImage("test", img)
