from gpiozero import Servo
from time import sleep

# servo = Servo(12)
servo = Servo(12, min_pulse_width=0.00054, max_pulse_width=0.0024) #0~180도 범위로 늘림

while True:
    servo.mid()
    print("mid")
    sleep(1)
    
    servo.min()
    print("min")
    sleep(1)
    
    servo.mid()
    print("mid")
    sleep(0.5)
    
    servo.max()
    print("max")
    sleep(1)