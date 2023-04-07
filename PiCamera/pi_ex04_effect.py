from picamera import PiCamera
from time import sleep

cam = PiCamera()

cam.start_preview()
for effect in cam.IMAGE_EFFECTS:
    cam.image_effect = effect
    cam.annotate_text = "Effect /%s/" %effect
    sleep(5)
    
cam.stop_preview()