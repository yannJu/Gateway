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
3. ### [ex13_BTN.py](./ex13_BTN.py)
    - `Button` 모듈을 이용하여 실습 진행
    - _Pull up_ 이나 _Pull Down_ 은 어떻게 설정 ? 
        - `Button` 생성시 **pull_up = True** 가 default 로 지정
        - `True` : 내부 풀업
        - `False` : 풀다운
    - `when_pressed` 를 이용하여 **callback** 을 할 수 있다.
    - `Button` 생성시 **hold_time** 등을 이용하여 "얼마나 누르면 동작하는가" 에 대한 이벤트 처리가 가능
4. ### [ex14_Btn_Led.py](./ex14_Btn_Led.py)
    - `Button` 클릭시 `LED` 불 켜고, 떼면 끄기
    
        ```python
        led.source = btn
        ```
    - 위와같이 `Button`의 상태를 `LED`에 동기화
5. ### [ex15_LEDBoard.py](./ex15_LEDBoard.py)
    - 여러개의 `LED` 를 한번에 제어
    - **디지털** 로 제어하는데, 생성자에서 `pwm` 인자에 **True** 를 해주면 **아날로그** 출력 가능
6. ### [ex16_LEDBarGraph.py](./ex16_LEDBarGraph.py)
    - `LEDBarGraph` 라이브러리를 사용하여 `LED` 제어
7. ### [ex17_GRBLED.py](./ex17_GRBLED.py)
    - `3색 LED` 를 `RGELED`로 제어
### → **ex15-ex17** 을 보면 함수호출보다 `property` 의 `setter`를 이용하여 제어를 하고 있는 모습을 보임
8. ### [ex18_MotionSensor.py](./ex18_MotionSensor.py)
    - `PIR`센서를 이용한 실습
    - gpiozero 의 `MotionSensor` 모듈을 이용
    - 움직임이 감지됨에 따라 `LED` 제어
