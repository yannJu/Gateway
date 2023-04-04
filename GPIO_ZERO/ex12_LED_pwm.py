from gpiozero import PWMLED
from signal import pause

led = PWMLED(13)
led.pulse(fade_in_time=2, fade_out_time=1)

# pause()
# pause 대신 입력을 받아서 종료시키자. . !
input('종료할면 엔터를 누르세요 !')