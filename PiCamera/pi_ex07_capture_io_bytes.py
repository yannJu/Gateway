from io import BytesIO
from time import sleep
from picamera import PiCamera

my_stream = BytesIO()

cam = PiCamera()
cam.start_preview()

#warm up time
sleep(2)

cam.capture(my_stream, 'jpeg')

data = my_stream.getvalue()
print(len(data), type(data))