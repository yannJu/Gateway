import picamera
from time import sleep

with picamera.PiCamera() as cam:
    cam.resolution = (640, 480)
    cam.start_preview()

    for i in range(5):
        cam.annotate_text_size = 50
        cam.annotate_background = picamera.Color('blue')
        cam.annotate_foreground = picamera.Color('yellow')
        cam.annotate_text = "Im Yannjo !"
        sleep(5)
        
        cam.capture(f'./img/imageText_{i}.jpg')
        
    cam.stop_preview()
