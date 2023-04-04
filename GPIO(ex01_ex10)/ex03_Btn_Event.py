import RPi.GPIO as GPIO
import time

count = 0

def button_callback(channel):
    global count
    
    count += 1
    print("Button Pushed! : ", count)
    
button_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Event 방식으로 Falling 신호를 감지하면  callback 함수 실행
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback)

while True:
    time.sleep(0.1)