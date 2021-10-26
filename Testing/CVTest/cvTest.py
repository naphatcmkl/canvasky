import cv2
import numpy as np
from collections import deque

blue = [deque(maxlen=1024)]
green = [deque(maxlen=1024)]
red = [deque(maxlen=1024)]
yellow = [deque(maxlen=1024)]

capture = cv2.VideoCapture(0)
while True:

    # Read each frame from webcam
    success, frame = capture.read()

    # Flip the frame
    frame = cv2.flip(frame, 1)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

# colors = [(255, 0, 0), (255, 0, 255), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
# color = colors[0]
#
# width = int(capture.get(3))
# height = int(capture.get(4))
# # Create a blank canvas
# canvas = np.zeros((height, width, 3), np.uint8)
