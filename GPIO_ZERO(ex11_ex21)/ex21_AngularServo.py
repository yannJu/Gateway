from gpiozero import AngularServo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

#jittering 제어
factory = PiGPIOFactory(host = 'localhost')
servo = AngularServo(12, min_angle=-90, max_angle=90, 
                     min_pulse_width=0.00054, max_pulse_width=0.0024,
                     pin_factory = factory)

while True:
    servo.angle = -90
    sleep(2)
    
    servo.angle = 0
    sleep(2)
    
    servo.angle = 90
    sleep(2)
    
    servo.angle = 0
    sleep(2)