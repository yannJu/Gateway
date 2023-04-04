import RPi.GPIO as GPIO
import time

TRIG = 21
ECHO = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("Distance measurement in progress")

GPIO.output(TRIG, False)
print("Waiting for sensor to settle. . ")
time.sleep(2)

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        # time 갱신
        while GPIO.input(ECHO) == 0:
            start = time.time()
        while GPIO.input(ECHO) == 1:
            stop = time.time()
            
        check_time = stop - start
        distance = check_time * 34300 / 2
        print("Distance : %.1f cm" %distance)
        time.sleep(0.4)
        
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()