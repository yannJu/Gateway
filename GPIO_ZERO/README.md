# GATEWAY _ GPIO_ZERO 📰
---
1. ### [ex11_LED.py](./ex11_LED.py)
    - `GPIO_ZERO` 라이브러리를 이용하여 `LED` 센서를 쉽게 **On/Off** 혹은 **Blink** 할 수 있다.
    - 자동으로 `cleanup()` 을 해준다.
    - `blink()` 후 `pause()` 를 했음에도 계속 동작을 하는 이유?
        - `blink()`가 **thread** 동작을 하기 때문
    - `value` 를 이용하여 값을 변경 가능
2. ### [ex12_LED_pwm.py](./ex12_LED_pwm.py)
    - `PWMLED` 를 통해 `LED` 조절
    - `pause()` 가 없다면 **메인 스레드** 가 종료되어 프로그램이 죽게 된다.