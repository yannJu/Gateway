from time import sleep
from picamera import PiCamera

camera = PiCamera(resolution=(1280, 720), framerate = 30)

camera.capture_sequence([f'/home/yannju/Desktop/image{i:02d}.jpg' for i in range(10)])