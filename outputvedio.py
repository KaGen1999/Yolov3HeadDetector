import numpy as np
import cv2 as cv
from nets.yolo3 import yolo_body
from keras.layers import Input
from yolo import YOLO
from PIL import Image

yolo = YOLO()

cap = cv.VideoCapture('b.mp4')
video_frame_cnt = int(cap.get(7))
video_width = int(cap.get(3))
video_height = int(cap.get(4))
video_fps = int(cap.get(5))

fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv.VideoWriter('result2.mp4', fourcc, video_fps, (video_width, video_height))

# Define the codec and create VideoWriter object

c = 0
while (cap.isOpened()):
    c = c + 1
    ret, frame = cap.read()
    if ret == True and c % 10 == 0:
        # frame = cv.flip(frame,0)
        frame = Image.fromarray(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
        r_image = yolo.detect_image(frame)
        # r_image.save('./pic/'+str(c) + '.jpg')
        # write the flipped frame
        img = cv.cvtColor(np.asarray(r_image), cv.COLOR_RGB2BGR)
        for i in range(10):
            out.write(img)
    elif ret == False:
        break

cap.release()
out.release()
yolo.close_session()
