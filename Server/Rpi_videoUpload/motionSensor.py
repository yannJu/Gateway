import cv2
from gpiozero import MotionSensor
from signal import pause
from datetime import datetime
from time import sleep
from fileUpload import upload, notify_instrusion
from convert import convert

isStop = 1
recorder = None
cap = cv2.VideoCapture(0)
upload_url = "http://172.20.10.5:8000/iot/upload/"
fname = ""

def record():
    global isStop, recorder, fname
    
    isStop = 0
    
    frame_size = 640, 480
    startTime = datetime.now()
    fname = startTime.strftime('./data/%Y%m%d_%H_%M')

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    recorder = cv2.VideoWriter(fname + '.h264',  fourcc, 20.0, frame_size)
    
    notify_instrusion()

def stop():
    global isStop , recorder
    
    if (isStop == 0):
        isStop = 1
        print("Stop . . !")
        
        inputpath = fname + '.h264'
        outputpath = fname + '.mp4'
        convert(inputpath, outputpath)
        print(f"Convert . . /{inputpath}/")
        
        upload(outputpath, upload_url)
        print("Upload Success!")
        
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