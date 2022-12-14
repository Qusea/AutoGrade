a_x1 = 470
a_x2 = 354
print("a width: ", a_x1 - a_x2)

b_x1 = 352
b_x2 = 236
print("b width: ", b_x1 - b_x2)

c_x1 = 234
c_x2 = 118
print("c width: ", c_x1 - c_x2)

d_x1 = 116
d_x2 = 0
print("d width: ", d_x1 - d_x2)

print()

q1_y1 = 25
q1_y2 = 46
print("1 height: ", q1_y1 - q1_y2)

q2_y1 = 71
q2_y2 = 92
print("2 height: ", q2_y1 - q2_y2)

q3_y1 = 190
q3_y2 = 210
print("3 height: ", q3_y1 - q3_y2)

q4_y1 = 236
q4_y2 = 257
print("4 height: ", q4_y1 - q4_y2)

q5_y1 = 283
q5_y2 = 304
print("5 height: ", q5_y1 - q5_y2)

q6_y1 = 330
q6_y2 = 352
print("6 height: ", q6_y1 - q6_y2)

q7_y1 = 376
q7_y2 = 398
print("7 height: ", q7_y1 - q7_y2)

q8_y1 = 423
q8_y2 = 492
print("8 height: ", q8_y1 - q8_y2)

q9_y1 = 517
q9_y2 = 538
print("9 height: ", q9_y1 - q9_y2)

# print vertical distance between questions
for i in range(1, 9):
    print("q{} to q{}: {}".format(i, i + 1, eval("q{}_y1 - q{}_y2".format(i + 1, i))))

