from gpiozero import LEDBoard
from time import sleep
from signal import pause

# leds = LEDBoard(12, 16, 20, 21) #R, G, B, R
leds = LEDBoard(12, 16, 20, 21, pwm = True) #R, G, B, R

# 4개의 led 전체 Blink
# leds.on()
# sleep(1)
# leds.off()
# sleep(1)

# # 개별적인 값을 튜플로 setting
# leds.value = (1, 0, 1, 0)
# sleep(1)

# # 전체 led 블링크
# leds.blink()

# pause()

leds.value = (0.25, 0.5, 0.75, 1.0)
pause()