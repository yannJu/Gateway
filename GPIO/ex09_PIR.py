import RPi.GPIO as GPIO
import time

led_R = 21
led_B = 16
pir = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_R, GPIO.OUT)
GPIO.setup(led_B, GPIO.OUT)
GPIO.setup(pir, GPIO.IN)

print("PIR Ready . . .")
time.sleep(5)

try:
    while True:
        if GPIO.input(pir) == 1:
            GPIO.output(led_B, 1)
            GPIO.output(led_R, 0)
            print("Motion Detected -- !")
            time.sleep(0.2)
        
        if GPIO.input(pir) == 0:
            GPIO.output(led_R, 1)
            GPIO.output(led_B, 0)
            time.sleep(0.2)
            
except KeyboardInterrupt:
    print("Stopped By User")
    GPIO.cleanup()