import cv2
import numpy as np
from datetime import datetime

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

startTime = datetime.now()
fname = startTime.strftime('./data/%Y%m%d_%H_%M.mp4')

frame_size = 640, 480
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out1 = cv2.VideoWriter(fname, fourcc, 20.0, frame_size)

while True:
    ret, frame = cap.read()
    if not ret: break
    
    point = 30, 30
    date = datetime.today()
    strDate = date.strftime('REC . . %Y-%m-%d %H:%M:%S')
    cv2.putText(frame, strDate, point, font, 0.7, (0, 125, 125), 2, cv2.LINE_AA)
    
    cv2.imshow("test", frame)
    out1.write(frame)
    
    key = cv2.waitKey(25)
    if key == 27: break;
    
cv2.destroyAllWindows()