from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

# Create the in-memory stream
stream = BytesIO()
cam = PiCamera()

cam.start_preview()
sleep(1)

cam.capture(stream, format = 'jpeg')
stream.seek(0)

img = Image.open(stream)
img.show()