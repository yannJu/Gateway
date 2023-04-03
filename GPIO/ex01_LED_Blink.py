import RPi.GPIO as GPIO
import time

#set using Pin Num(BCM mode)
led_pin = 16 #GPIO 16 pin

#set GPIO pin mode
GPIO.setmode(GPIO.BCM)

# set IN/OUT
GPIO.setup(led_pin, GPIO.OUT)

for i in range(10):
    GPIO.output(led_pin, 1) #LED ON
    time.sleep(1)
    GPIO.output(led_pin, 0) #LED OFF
    time.sleep(1)
    
GPIO.cleanup()