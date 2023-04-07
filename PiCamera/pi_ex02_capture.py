import picamera
import time

with picamera.PiCamera() as cam:
    res = int(input("Resolution <1 ; 320x420, 2; 640x480, 3;1024x768>? >> "))
    
    if res == 3: cam.resolution = (1024, 768)
    elif res == 2: cam.resolution = (640, 480)
    else: cam.resolution = (320, 420)
    
    filename = input("Input File Name >> ")
    
    cam.start_preview()
    
    time.sleep(1)
    cam.stop_preview()
    
    cam.capture('./img/' + filename + '.jpg')