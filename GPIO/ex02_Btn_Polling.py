import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀의 번호 선정
button_pin = 26

# 버튼 눌린 횟수 ck
count = 0 

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(button_pin) == GPIO.LOW:
            print("Button Pushed !")
            count += 1
        time.sleep(0.1)
finally:
    print("Button Click : ", count)
    GPIO.cleanup()