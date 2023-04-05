from gpiozero import DistanceSensor, LED
from signal import pause

sensor = DistanceSensor(12, 16, max_distance=1, threshold_distance=0.2)
led = LED(21)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off

print(f"Distance is {sensor.distance * 100}cm")
pause()