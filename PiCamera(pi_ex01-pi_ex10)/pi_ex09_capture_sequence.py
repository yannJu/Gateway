from time import sleep
from picamera import PiCamera

# 1.
# camera = PiCamera(resolution=(1280, 720), framerate = 30)
# camera.capture_sequence([f'/home/yannju/Desktop/image{i:02d}.jpg' for i in range(10)])

# 2.
camera = PiCamera()
sleep(2)

# 계속 찍힘
for filename in camera.capture_continuous('/home/yannju/Desktop/img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    sleep(10)