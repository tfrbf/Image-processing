import cv2 as cv
import time 

cam = cv.VideoCapture(1)
num_frames = 120

start = time.time()

for i in range(0, num_frames):
    ret, frame = cam.read()

end = time.time()

seconds = end - start

fps = num_frames / seconds

# Retrieve frame width and height
width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

print("Resolution is: (%d, %d) pixels" % (width, height))
print("FPS is:", int(fps))

cam.release()
