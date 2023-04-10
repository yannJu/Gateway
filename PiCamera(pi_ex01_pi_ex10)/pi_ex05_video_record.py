from subprocess  import call
import os
import picamera
from video_util import convert

# def convert(src, dst):
#     command =  f'MP4Box -add {src} {dst}'
#     call([command], shell = True)
#     os.remove(src)

filename = ""
with picamera.PiCamera() as cam:
    res = int(input("Resolution (1: 320x240, 2: 640x480, 3: 1024x768) > > "))
    
    if res == 3: cam.resolution = (1024, 768)
    elif res == 2: cam.resolution = (640, 480)
    else: cam.resolution = (320, 240)
    
    filename = "/home/yannju/Desktop/" + input("Input File Name >> ")

    ## fps
    cam.framerate = 15 #1초에 15
    cam.start_preview()
    
    # 여기부터 preview 와 연관 없음======
    cam.start_recording(output = filename + '.h264')
    cam.wait_recording(5)
    cam.stop_recording()
    
    cam.stop_preview()
    
src = filename + '.h264'
dst = filename + '.mp4'

convert(src, dst)