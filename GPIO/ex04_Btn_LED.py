import RPi.GPIO as GPIO
import time

# 버튼 입력에 따라 LED 상태 변경

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

# GPIO 핀 설정
led_pin = 16
button_pin = 26
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

light_on = False

def led_callback(channel):
    global light_on
    
    if (light_on):
        GPIO.output(led_pin, 0)
        print("LED /OFF/!")
    else:
        GPIO.output(led_pin, 1)
        print("LED /ON/!")
    
    light_on = not light_on
    
try:
    GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=led_callback, 
                          bouncetime = 300)
    # GPIO.output(led_pin, 0)sgit
    while True:
        time.sleep(0.1)
        
finally:
    GPIO.cleanup()