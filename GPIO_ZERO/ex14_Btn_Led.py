from gpiozero import Button, LED
from signal import pause

led = LED(20)
led = LED(21)
btn  = Button(26)

btn.when_pressed = led.on
btn.when_released = led.off

# led.source = btn
pause()