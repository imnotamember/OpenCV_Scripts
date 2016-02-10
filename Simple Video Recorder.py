'''
#import numpy as np
import cv2

w = 640
h = 480

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)


while True:
    ret, img = cap.read()
    cv2.imshow('capture', img)
    ch = 0xFF & cv2.waitKey(1)
    if ch == 27:
        break
cv2.destroyAllWindows()

capture = cv2.VideoCapture(0)

# video recorder
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.cv.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
video_writer = cv2.VideoWriter("output.avi", fourcc, 20, (680, 480))
i = 0
# record video
while (capture.isOpened()):
    i += 1
    ret, frame = capture.read()
    if ret:
        video_writer.write(frame)
        cv2.imshow('Video Stream', frame)
    elif i > 100:
        break
    else:
        break

capture.release()
video_writer.release()
cv2.destroyAllWindows()
'''
import numpy as np
import cv2
try:
    import pygame
    timer = pygame.time
    timer.Clock()
except:
    pass

face_cascade = cv2.CascadeClassifier('/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
height, width = frame.shape[:2]

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fourcc = cv2.cv.CV_FOURCC(*'MJPG')
out = cv2.VideoWriter('C:/outpuasdft.avi', fourcc, 7, (width, height))
# t0 = timer.get_ticks()
i = 0
while cap.isOpened():
    # time_diff = timer.get_ticks() - t0
    # if time_diff >= 11000:
    #     break
    ret, frame = cap.read()
    if ret:
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# print time_diff
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture('C:/outpuasdft.avi')
print cap.get(7)
