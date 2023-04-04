import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(21, 100)

Frq = [262, 294, 330, 349, 392, 440, 493, 523]
speed = 0.5

p.start(10)

try:
    while True:
        for fq in Frq:
            p.ChangeFrequency(fq)
            time.sleep(speed)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()