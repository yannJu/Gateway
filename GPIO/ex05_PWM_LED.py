import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT) # 16번핀(LED)

p = GPIO.PWM(16, 50) # 16번핀(LED) 를 50Hz 로
p.start(0) # Duty 비 0, PWM 시작

try:
    while True:
        # 증가
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        #감소
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()