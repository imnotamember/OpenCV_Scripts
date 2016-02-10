import numpy as np
import cv2

# face_cascade = cv2.CascadeClassifier('C:\Users\Joshua\PycharmProjects\OpenCV Scripts\lbpcascades\lbpcascade_frontalface.xml')
face_cascade = cv2.CascadeClassifier('C:\Users\Joshua\PycharmProjects\OpenCV Scripts\haarcascades\haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('C:\Users\Joshua\PycharmProjects\OpenCV Scripts\haarcascades\haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)
width = 640
height = 480
backup_rectangle = ((0, 0), (0 + width, 0 + height), (0, 0, 0), 2)
blue_offset = 255
green_offset = 255
red_offset = 255
while cap.isOpened():
    ret, img = cap.read()
    if ret:
        # write the flipped frame
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 6)
        #img = cv2.blur(img, (5, 5))
        i = 0
        for (x, y, w, h) in faces:
            i += 1
            # img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            head_center_w = x + (w / 2)
            head_center_h = y + (h / 2)
            screen_center_w = width / 2
            screen_center_h = height / 2
            blue_offset = abs(screen_center_w - head_center_w)
            red_offset = abs(screen_center_h - head_center_h)
            if blue_offset > 255:
                blue_offset = 255
            if red_offset > 255:
                red_offset = 255
            green_offset = (blue_offset + red_offset) / 2
            if green_offset > 255:
                green_offset = 255
            backup_rectangle = ((x, y), (x + w, y + h), (blue_offset, 255, red_offset), 10)
            img = cv2.rectangle(img, *backup_rectangle)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            # eyes = eye_cascade.detectMultiScale(roi_gray)
            # for (ex, ey, ew, eh) in eyes:
            #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)
        if i == 0:
            img = cv2.rectangle(img, *backup_rectangle)
        img = cv2.flip(img, 1)
        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()