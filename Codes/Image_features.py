import cv2 as cv
import time 

cam = cv.VideoCapture(0)
num_frames = 120

start = time.time()

for i in range(0, num_frames):
    ret, frame = cam.read()

end = time.time()

secondes = end - start

fps = num_frames / 120

print("Resplution is:  (%d, %d) Pixels" %(cam.get(3), cam.get(4)))
print("FPS is: ", int(fps))

cam.release()