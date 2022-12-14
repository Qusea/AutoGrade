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
q1_tr1 = (469, 25)
q1_tl1 = (353, 25)
q1_br1 = (469, 46)
q1_bl1 = (353, 46)

q1_tr2 = (351, 25)
q1_tl2 = (235, 25)
q1_br2 = (351, 46)
q1_bl2 = (235, 46)

q1_tr3 = (233, 25)
q1_tl3 = (117, 25)
q1_br3 = (233, 46)
q1_bl3 = (117, 46)

q1_tr4 = (115, 25)
q1_tl4 = (0, 25)
q1_br4 = (115, 46)
q1_bl4 = (0, 46)

# make question 2 boxes
q2_tr1 = (469, 71)
q2_tl1 = (353, 71)
q2_br1 = (469, 92)
q2_bl1 = (353, 92)

q2_tr2 = (351, 71)
q2_tl2 = (235, 71)
q2_br2 = (351, 92)
q2_bl2 = (235, 92)

q2_tr3 = (233, 71)
q2_tl3 = (117, 71)
q2_br3 = (233, 92)
q2_bl3 = (117, 92)

q2_tr4 = (115, 71)
q2_tl4 = (0, 71)
q2_br4 = (115, 92)
q2_bl4 = (0, 92)

# make question 3 boxes
q3_tr1 = (469, 190)
q3_tl1 = (353, 190)
q3_br1 = (469, 210)
q3_bl1 = (353, 210)

q3_tr2 = (351, 190)
q3_tl2 = (235, 190)
q3_br2 = (351, 210)
q3_bl2 = (235, 210)

q3_tr3 = (233, 190)
q3_tl3 = (117, 190)
q3_br3 = (233, 210)
q3_bl3 = (117, 210)

q3_tr4 = (115, 190)
q3_tl4 = (0, 190)
q3_br4 = (115, 210)
q3_bl4 = (0, 210)

# make question 4 boxes
q4_tr1 = (469, 236)
q4_tl1 = (353, 236)
q4_br1 = (469, 257)
q4_bl1 = (353, 257)

q4_tr2 = (351, 236)
q4_tl2 = (235, 236)
q4_br2 = (351, 257)
q4_bl2 = (235, 257)

q4_tr3 = (233, 236)
q4_tl3 = (117, 236)
q4_br3 = (233, 257)
q4_bl3 = (117, 257)

q4_tr4 = (115, 236)
q4_tl4 = (0, 236)
q4_br4 = (115, 257)
q4_bl4 = (0, 257)

# make question 5 boxes
q5_tr1 = (469, 283)
q5_tl1 = (353, 283)
q5_br1 = (469, 304)
q5_bl1 = (353, 304)

q5_tr2 = (351, 283)
q5_tl2 = (235, 283)
q5_br2 = (351, 304)
q5_bl2 = (235, 304)

q5_tr3 = (233, 283)
q5_tl3 = (117, 283)
q5_br3 = (233, 304)
q5_bl3 = (117, 304)

q5_tr4 = (115, 283)
q5_tl4 = (0, 283)
q5_br4 = (115, 304)
q5_bl4 = (0, 304)

# make question 6 boxes
q6_tr1 = (469, 330)
q6_tl1 = (353, 330)
q6_br1 = (469, 352)
q6_bl1 = (353, 352)

q6_tr2 = (351, 330)
q6_tl2 = (235, 330)
q6_br2 = (351, 352)
q6_bl2 = (235, 352)

q6_tr3 = (233, 330)
q6_tl3 = (117, 330)
q6_br3 = (233, 352)
q6_bl3 = (117, 352)

q6_tr4 = (115, 330)
q6_tl4 = (0, 330)
q6_br4 = (115, 352)
q6_bl4 = (0, 352)

# make question 7 boxes
q7_tr1 = (469, 376)
q7_tl1 = (353, 376)
q7_br1 = (469, 398)
q7_bl1 = (353, 398)

q7_tr2 = (351, 376)
q7_tl2 = (235, 376)
q7_br2 = (351, 398)
q7_bl2 = (235, 398)

q7_tr3 = (233, 376)
q7_tl3 = (117, 376)
q7_br3 = (233, 398)
q7_bl3 = (117, 398)

q7_tr4 = (115, 376)
q7_tl4 = (0, 376)
q7_br4 = (115, 398)
q7_bl4 = (0, 398)

# make question 8 boxes (3x height of other questions)
q8_tr1 = (469, 423)
q8_tl1 = (353, 423)
q8_br1 = (469, 492)
q8_bl1 = (353, 492)

q8_tr2 = (351, 423)
q8_tl2 = (235, 423)
q8_br2 = (351, 492)
q8_bl2 = (235, 492)

q8_tr3 = (233, 423)
q8_tl3 = (117, 423)
q8_br3 = (233, 492)
q8_bl3 = (117, 492)

q8_tr4 = (115, 423)
q8_tl4 = (0, 423)
q8_br4 = (115, 492)
q8_bl4 = (0, 492)

# make question 9 boxes
q9_tr1 = (469, 517)
q9_tl1 = (353, 517)
q9_br1 = (469, 540)
q9_bl1 = (353, 540)

q9_tr2 = (351, 517)
q9_tl2 = (235, 517)
q9_br2 = (351, 540)
q9_bl2 = (235, 540)

q9_tr3 = (233, 517)
q9_tl3 = (117, 517)
q9_br3 = (233, 540)
q9_bl3 = (117, 540)

q9_tr4 = (115, 517)
q9_tl4 = (0, 517)
q9_br4 = (115, 540)
q9_bl4 = (0, 540)




# display question 1 answers
img = cv2.rectangle(img, q1_tr1, q1_bl1, color1)
img = cv2.rectangle(img, q1_tr2, q1_bl2, color2)
img = cv2.rectangle(img, q1_tr3, q1_bl3, color3)
img = cv2.rectangle(img, q1_tr4, q1_bl4, color4)

# display question 2 answers
img = cv2.rectangle(img, q2_tr1, q2_bl1, color2)
img = cv2.rectangle(img, q2_tr2, q2_bl2, color3)
img = cv2.rectangle(img, q2_tr3, q2_bl3, color4)
img = cv2.rectangle(img, q2_tr4, q2_bl4, color1)

# display question 3 answers
img = cv2.rectangle(img, q3_tr1, q3_bl1, color3)
img = cv2.rectangle(img, q3_tr2, q3_bl2, color4)
img = cv2.rectangle(img, q3_tr3, q3_bl3, color1)
img = cv2.rectangle(img, q3_tr4, q3_bl4, color2)

# display question 4 answers
img = cv2.rectangle(img, q4_tr1, q4_bl1, color4)
img = cv2.rectangle(img, q4_tr2, q4_bl2, color1)
img = cv2.rectangle(img, q4_tr3, q4_bl3, color2)
img = cv2.rectangle(img, q4_tr4, q4_bl4, color3)

# display question 5 answers
img = cv2.rectangle(img, q5_tr1, q5_bl1, color1)
img = cv2.rectangle(img, q5_tr2, q5_bl2, color2)
img = cv2.rectangle(img, q5_tr3, q5_bl3, color3)
img = cv2.rectangle(img, q5_tr4, q5_bl4, color4)

# display question 6 answers
img = cv2.rectangle(img, q6_tr1, q6_bl1, color2)
img = cv2.rectangle(img, q6_tr2, q6_bl2, color3)
img = cv2.rectangle(img, q6_tr3, q6_bl3, color4)
img = cv2.rectangle(img, q6_tr4, q6_bl4, color1)

# display question 7 answers
img = cv2.rectangle(img, q7_tr1, q7_bl1, color3)
img = cv2.rectangle(img, q7_tr2, q7_bl2, color4)
img = cv2.rectangle(img, q7_tr3, q7_bl3, color1)
img = cv2.rectangle(img, q7_tr4, q7_bl4, color2)

# display question 8 answers
img = cv2.rectangle(img, q8_tr1, q8_bl1, color4)
img = cv2.rectangle(img, q8_tr2, q8_bl2, color1)
img = cv2.rectangle(img, q8_tr3, q8_bl3, color2)
img = cv2.rectangle(img, q8_tr4, q8_bl4, color3)

# display question 9 answers
img = cv2.rectangle(img, q9_tr1, q9_bl1, color1)
img = cv2.rectangle(img, q9_tr2, q9_bl2, color2)
img = cv2.rectangle(img, q9_tr3, q9_bl3, color3)
img = cv2.rectangle(img, q9_tr4, q9_bl4, color4)


showImage("test", img)
