''' For testing purposes only - test functions, ideas. '''

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("unsolved_puzzle.png")


# Show grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Show edges only
canny = cv.Canny(img, 125, 175)

# Resize image
resized = cv.resize(img, (500,500))

# cv.imshow('Unsolved puzzle', img)
cv.imshow('Unsolved puzzle', resized)

cv.waitKey(0)