import cv2 as cv

img = cv.imread("Images/tess.jpg")
cv.imshow("TES", img)

print("Diemnsions: ", img.shape)
print("Total Sub - Pixels: ", img.size)
print("Resolution: ", img.shape[1],img.shape[0])
print("Total Pixels: ", img.size / 3)
print("dtype: ", img.dtype)

cv.waitKey()
cv.destroyAllWindows()