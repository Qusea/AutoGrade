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
q1start1 = (469, 25)
q1end1 = (353, 46)

q1start2 = (351, 25)
q1end2 = (235, 46)

q1start3 = (233, 25)
q1end3 = (117, 46)

q1start4 = (115, 25)
q1end4 = (0, 46)

# make question 2 boxes
q2start1 = (469, 71)
q2end1 = (353, 92)

q2start2 = (351, 71)
q2end2 = (235, 92)

q2start3 = (233, 71)
q2end3 = (117, 92)

q2start4 = (115, 71)
q2end4 = (0, 92)

# make question 3 boxes
q3start1 = (469, 190)
q3end1 = (353, 210)

q3start2 = (351, 190)
q3end2 = (235, 210)

q3start3 = (233, 190)
q3end3 = (117, 210)

q3start4 = (115, 190)
q3end4 = (0, 210)

# make question 4 boxes
q4start1 = (469, 236)
q4end1 = (353, 257)

q4start2 = (351, 236)
q4end2 = (235, 257)

q4start3 = (233, 236)
q4end3 = (117, 257)

q4start4 = (115, 236)
q4end4 = (0, 257)

# make question 5 boxes
q5start1 = (469, 283)
q5end1 = (353, 304)

q5start2 = (351, 283)
q5end2 = (235, 304)

q5start3 = (233, 283)
q5end3 = (117, 304)

q5start4 = (115, 283)
q5end4 = (0, 304)

# make question 6 boxes
q6start1 = (469, 330)
q6end1 = (353, 352)

q6start2 = (351, 330)
q6end2 = (235, 352)

q6start3 = (233, 330)
q6end3 = (117, 352)

q6start4 = (115, 330)
q6end4 = (0, 352)

# make question 7 boxes
q7start1 = (469, 376)
q7end1 = (353, 398)

q7start2 = (351, 376)
q7end2 = (235, 398)

q7start3 = (233, 376)
q7end3 = (117, 398)

q7start4 = (115, 376)
q7end4 = (0, 398)

# make question 8 boxes (3x height of other questions)
q8start1 = (469, 423)
q8end1 = (353, 492)

q8start2 = (351, 423)
q8end2 = (235, 492)

q8start3 = (233, 423)
q8end3 = (117, 492)

q8start4 = (115, 423)
q8end4 = (0, 492)

# make question 9 boxes
q9start1 = (469, 517)
q9end1 = (353, 540)

q9start2 = (351, 517)
q9end2 = (235, 540)

q9start3 = (233, 517)
q9end3 = (117, 540)

q9start4 = (115, 517)
q9end4 = (0, 540)


# display question 1 answers
img = cv2.rectangle(img, q1start1, q1end1, color1)
img = cv2.rectangle(img, q1start2, q1end2, color2)
img = cv2.rectangle(img, q1start3, q1end3, color3)
img = cv2.rectangle(img, q1start4, q1end4, color4)

# display question 2 answers
img = cv2.rectangle(img, q2start1, q2end1, color2)
img = cv2.rectangle(img, q2start2, q2end2, color3)
img = cv2.rectangle(img, q2start3, q2end3, color4)
img = cv2.rectangle(img, q2start4, q2end4, color1)

# display question 3 answers
img = cv2.rectangle(img, q3start1, q3end1, color3)
img = cv2.rectangle(img, q3start2, q3end2, color4)
img = cv2.rectangle(img, q3start3, q3end3, color1)
img = cv2.rectangle(img, q3start4, q3end4, color2)

# display question 4 answers
img = cv2.rectangle(img, q4start1, q4end1, color4)
img = cv2.rectangle(img, q4start2, q4end2, color1)
img = cv2.rectangle(img, q4start3, q4end3, color2)
img = cv2.rectangle(img, q4start4, q4end4, color3)

# display question 5 answers
img = cv2.rectangle(img, q5start1, q5end1, color1)
img = cv2.rectangle(img, q5start2, q5end2, color2)
img = cv2.rectangle(img, q5start3, q5end3, color3)
img = cv2.rectangle(img, q5start4, q5end4, color4)

# display question 6 answers
img = cv2.rectangle(img, q6start1, q6end1, color2)
img = cv2.rectangle(img, q6start2, q6end2, color3)
img = cv2.rectangle(img, q6start3, q6end3, color4)
img = cv2.rectangle(img, q6start4, q6end4, color1)

# display question 7 answers
img = cv2.rectangle(img, q7start1, q7end1, color3)
img = cv2.rectangle(img, q7start2, q7end2, color4)
img = cv2.rectangle(img, q7start3, q7end3, color1)
img = cv2.rectangle(img, q7start4, q7end4, color2)

# display question 8 answers
img = cv2.rectangle(img, q8start1, q8end1, color4)
img = cv2.rectangle(img, q8start2, q8end2, color1)
img = cv2.rectangle(img, q8start3, q8end3, color2)
img = cv2.rectangle(img, q8start4, q8end4, color3)

# display question 9 answers
img = cv2.rectangle(img, q9start1, q9end1, color1)
img = cv2.rectangle(img, q9start2, q9end2, color2)
img = cv2.rectangle(img, q9start3, q9end3, color3)
img = cv2.rectangle(img, q9start4, q9end4, color4)

showImage("test", img)
