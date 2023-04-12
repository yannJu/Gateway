import io
import time
import numpy as np
import cv2

class MJpegStreamCam:
    def __init__(self, framerate = 25, width = 640, height = 480):
        self.size = (width, height)
        self.framerate =  framerate
        
        #camera Setting
        self.camera = cv2.VideoCapture(0)# 카메라 프레임 설정

    def snapshot(self):
        retval, frame = self.camera.read()     # 카메라에서 프레임 캡쳐
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 80]
        is_success, jpg = cv2.imencode(".jpg", frame, encode_param)
        
        return jpg.tobytes()
        
    def __iter__(self):
        while True:
            ret, frame = self.camera.read()
            if not ret: break
            
            en_ret, en_frame = cv2.imencode('.jpg', frame)
            if not en_ret: break
            img = en_frame.tobytes()
            
            yield(b'--myboundary\n'
                    b'Content-Type:image/jpeg\n'
                    b'Content-Length: ' + f"{len(img)}".encode() + b'\n'
                    b'\n' + img + b'\n')
            #time.sleep(1/self.framerate)