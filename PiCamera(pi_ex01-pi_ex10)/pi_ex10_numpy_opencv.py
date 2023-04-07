import time
from picamera import PiCamera
import numpy as np
import cv2

with PiCamera() as cam:
    cam.resolution = (640, 480)
    
    img = np.empty((480, 640, 3), dtype = np.uint8)
    
    #opencv Video Capture 와 같은 기능
    while True:
        # 1초에 몇장 찍히는지 ck
        start = time.time()
        
        cam.capture(img, 'bgr', use_video_port = True)
        cv2.imshow('frame', img)
        if cv2.waitKey(1) == 27: break
        
        end = time.time()
        fps = 1 / (end - start)
        
        print(f"fps : /{fps:0.1f}/")