import cv2
import numpy as np

img = cv2.imread(
    "/Users/quseasaif/Documents/Misk Data Science/Capstone/AutoGrade/data/test1/test1-blank-paper.jpg"
)


def showImage(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)


q1start1 = (469, 25)
q1end1 = (353, 46)
color1 = (0, 255, 255)

q1start2 = (351, 25)
q1end2 = (235, 46)
color2 = (0, 255, 0)

q1start3 = (233, 25)
q1end3 = (117, 46)
color3 = (0, 0, 255)

q1start4 = (115, 25)
q1end4 = (0, 46)
color4 = (255, 0, 0)

q2start1 = (469, 71)
q2end1 = (353, 92)

q2start2 = (351, 71)
q2end2 = (235, 92)

q2start3 = (233, 71)
q2end3 = (117, 92)

q2start4 = (115, 71)
q2end4 = (0, 92)

q3start1 = (469, 190)
q3end1 = (353, 210)

q3start2 = (351, 190)
q3end2 = (235, 210)

q3start3 = (233, 190)
q3end3 = (117, 210)

q3start4 = (115, 190)
q3end4 = (0, 210)

img = cv2.rectangle(img, q1start1, q1end1, color1)
img = cv2.rectangle(img, q1start2, q1end2, color2)
img = cv2.rectangle(img, q1start3, q1end3, color3)
img = cv2.rectangle(img, q1start4, q1end4, color4)

img = cv2.rectangle(img, q2start1, q2end1, color2)
img = cv2.rectangle(img, q2start2, q2end2, color3)
img = cv2.rectangle(img, q2start3, q2end3, color4)
img = cv2.rectangle(img, q2start4, q2end4, color1)

img = cv2.rectangle(img, q3start1, q3end1, color3)
img = cv2.rectangle(img, q3start2, q3end2, color4)
img = cv2.rectangle(img, q3start3, q3end3, color1)
img = cv2.rectangle(img, q3start4, q3end4, color2)

showImage("test", img)
