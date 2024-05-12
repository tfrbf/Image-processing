import cv2 as cv
import numpy as np

img = cv.imread("Images/tess.jpg")

(B,G,R) = cv.split(img)

splited = np.hstack([B,G,R])

#splited = cv.flip(splited, 1)

cv.imshow("img", splited)


cv.waitKey()
cv.destroyAllWindows()