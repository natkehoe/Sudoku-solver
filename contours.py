import cv2 as cv

img = cv.imread('unsolved_puzzle.png')

canny = cv.Canny(img, 125, 175)


# Find contours of image
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE )
    # contours - lists all contours coordinates found in image
    # hierarchies - the hierarchical representation of each contour; contours inside of contours
    # RETR_LIST - return all contours
    # RETR_EXTERNAL - return all external contours
    # RETR_TREE - return all hierarchical contours
    # CHAIN_APPROX_NONE - return all contours
    # CHAIN_APPROX_SIMPLE - define i.e. a line by its two endpoints

print(f'{len(contours)} countours were found')

cv.imshow('Canny Edges', canny)
cv.waitKey(0)