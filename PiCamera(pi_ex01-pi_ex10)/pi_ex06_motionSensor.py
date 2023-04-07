from gpiozero import MotionSensor
import picamera
from datetime import datetime
from video_util import convert
from signal import pause
from time import sleep

cam = picamera.PiCamera()
cam.framerate = 15 #1초에 15
filename = "/home/yannju/Desktop/"

def record():
    global filename
    
    print("Recording Start!")
    cam.start_preview()
    
    now = datetime.today()
    nowStr = now.strftime("%Y-%m-%d %H:%M:%S")
    filename += nowStr
    cam.annotate_text = "REC . . . " + nowStr
    
    cam.start_recording(output = filename + '.h264')

def stop():
    print("Recording End . .")
    cam.stop_preview()
    cam.stop_recording()
    
    src = filename + '.h264'
    dst = filename + '.mp4'
    
    convert(src, dst)

pir = MotionSensor(12)
pir.when_motion = record
pir.when_no_motion = stop

pause()