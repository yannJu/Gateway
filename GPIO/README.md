# GATEWAY _ GPIO 📡
---
1. ### [ex01_LED_Blink.py](./ex01_LED_Blink.py)
	- `GPIO` 핀을 **연결** 하여 `LED` 조절
    - 현재는 입력되지 않았지만 **keyboard interrupt** 를 받게될 경우의 처리 또한 진행되어야 한다.
    	- `GPIO.cleanup()` 이 현재는 **에러** 발생시 동작하지 않는다.
    - ~~따라서 `try-finally` 문을 이용하여 무조건 `finally` 절이 수행되도록 한다.~~ **적용완료**
2. ### [./ex02_Btn_Polling.py](./ex02_Btn_Polling.py)
    - `GPIO` 핀을 **연결** 하여 `Button` 입력 받기
3. ### [./ex03_Btn_Event.py](./ex03_Btn_Event.py)
    - `Button` 입력을 통해 **callback** 함수 연결
    - `add_event_detect` 를 이용하여 **엣지** 에 따라 `callback` 함수가 호출되도록 한다.
4. ### [ex04_Btn_LED.py](./ex04_Btn_LED.py)
    - `Button` 입력을 통해 `LED` 제어
    - **ex01** ~ **ex03** 활용
5. ### [ex05_PWM_LED.py](./ex05_PWM_LED.py)
    - **아날로그** 입출력을 위해 `PWM` 사용
    - `LED` 밝기가 커졌다가 줄어드는 동작 반복
6. ### [ex06_PWM_Buzzer.py](./ex06_PWM_Buzzer.py)
    - `수동 부저` 를 활용한 실습
    - `ChangDutyCycle` 의 경우 **0-100** 까지만 지정이 가능
    - 따라서 `ChangeFrequency` 를 이용하여 **주파수** 를 변경