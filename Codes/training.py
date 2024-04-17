import cv2 as cv
import glob

filepath = glob.glob("*.jpg")

print("Your images: ", filepath)

for image_path in filepath:
    img = cv.imread(image_path)
    cv.imshow("Your image with glob:", img)
    cv.waitKey(1000)  # Wait until a key is pressed

cv.destroyAllWindows()
