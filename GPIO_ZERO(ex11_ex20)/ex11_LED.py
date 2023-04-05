from gpiozero import LED
from time import sleep
from signal import pause

red = LED(13)

# while True:
#     red.on()
#     sleep(1)
#     red.off()
#     sleep(1)
    
red.blink()
sleep(5)

red.blink(on_time=0.2, off_time=1)
sleep(5)

red.value = 0
sleep(5)
red.value = 1
print(red.value)
sleep(3)
