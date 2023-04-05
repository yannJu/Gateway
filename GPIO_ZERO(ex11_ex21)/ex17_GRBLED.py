from gpiozero import RGBLED
from time import sleep

led = RGBLED(red = 12, green = 16, blue = 25)

led.red = 1 #full red
sleep(1)

led.red = 0.5 #half red
sleep(1)

led.color = (0, 1, 0) #full green
sleep(1)
led.color = (1, 0, 1) #full red, blue(magenta)
sleep(1)
led.color = (1, 1, 0) #full yellow
sleep(1)
led.color = (0, 1, 1) #full cyan
sleep(1)
led.color = (1, 1, 1) #full white
sleep(1)
led.color = (0, 0, 0) #off
sleep(1)

# 서서히 밝아지도록
for n in range(100):
    led.blue = n / 100
    sleep(0.1)