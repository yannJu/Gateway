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
pause()