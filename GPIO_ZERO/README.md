# GATEWAY _ GPIO_ZERO 📰
---
1. ### [ex11_LED.py](./ex11_LED.py)
    - `GPIO_ZERO` 라이브러리를 이용하여 `LED` 센서를 쉽게 **On/Off** 혹은 **Blink** 할 수 있다.
    - 자동으로 `cleanup()` 을 해준다.
    - `blink()` 후 `pause()` 를 했음에도 계속 동작을 하는 이유?
        - `blink()`가 **thread** 동작을 하기 때문