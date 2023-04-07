import cv2
from gpiozero import MotionSensor
from signal import pause
from datetime import datetime
from time import sleep

isStop = 1
recorder = None
cap = cv2.VideoCapture(1)

def record():
    global isStop, recorder
    
    isStop = 0
    
    frame_size = 640, 480
    startTime = datetime.now()
    fname = startTime.strftime('./data/%Y%m%d_%H_%M.mp4')

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    recorder = cv2.VideoWriter(fname,  fourcc, 20.0, frame_size)

def stop():
    global isStop , recorder
    
    isStop = 1
    print("Stop . . !")
    
    sleep(0.1)
    if recorder: recorder.release() 
    recorder = None   

pir = MotionSensor(12)

pir.when_motion = record
pir.when_no_motion = stop
    
while True:
    ret, frame = cap.read()
    if not ret: break
    if isStop:
        sleep(0.1)
        continue
    
    print("Recording . . .")
    now = datetime.now()
    txt = now.strftime('REC . .%Y-%m-%d %H:%M:%S')
    cv2.putText(frame, txt, (30, 30), cv2.FONT_ITALIC, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
    
    recorder.write(frame)
    cv2.waitKey(50)