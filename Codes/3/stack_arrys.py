import cv2 as cv
import numpy as np

img1 = cv.imread("Images/tess.jpg")
img2 = cv.imread("Images/tess.jpg")

attach = np.hstack([img1, img2])
#attach = np.vstack([img1, img2])


cv.imshow("Attached images", attach)

cv.waitKey()
cv.destroyAllWindows()