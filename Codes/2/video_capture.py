import cv2 as cv

film = cv.VideoCapture(0)

while(1):
    ret, frame = film.read()

    if ret == True:
        cv.imshow("Movie", frame)

    if cv.waitKey(1) == 27:
        break

film.release()
cv.destroyAllWindows()