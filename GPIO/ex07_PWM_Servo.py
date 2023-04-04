import RPi.GPIO as GPIO
import time

servo_pin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50)
servo.start(0)

try:
    while True:
        # servo.ChangeDutyCycle(7.5) # 90도
        # print("90")
        # time.sleep(1)
        
        # servo.ChangeDutyCycle(12.5) # 180도
        # print("180")
        # time.sleep(1)
        
        # servo.ChangeDutyCycle(2.5) # 0도
        # print("0")
        # time.sleep(1)
        
        angle = float(input('각도 : '))
        dc = (10 / 180) * angle + 2.5
        
        servo.ChangeDutyCycle(dc)
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()