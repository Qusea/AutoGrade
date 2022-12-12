import cv2
import numpy as np

inputImage = cv2.imread(
    "/Users/quseasaif/Documents/Misk Data Science/Capstone/AutoGrade/data/test1/test1-blank-paper.jpg"
)

# Store a deeep copy for results:
inputCopy = inputImage.copy()

# Convert BGR to grayscale:
grayInput = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)

# Threshold via Otsu
_, binaryImage = cv2.threshold(
    grayInput, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# Set kernel (structuring element) size:
kernelSize = (8, 8)

# Set operation iterations:
opIterations = 3

# Get the structuring element:
morphKernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)

# Perform Dilate:
dilateImage = cv2.morphologyEx(
    binaryImage,
    cv2.MORPH_DILATE,
    morphKernel,
    None,
    None,
    opIterations,
    cv2.BORDER_REFLECT101,
)

cv2.imshow("Dilate", dilateImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
