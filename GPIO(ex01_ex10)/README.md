# GATEWAY _ GPIO 📡
---
1. ### [ex01_LED_Blink.py](./ex01_LED_Blink.py)
	- `GPIO` 핀을 **연결** 하여 `LED` 조절
    - 현재는 입력되지 않았지만 **keyboard interrupt** 를 받게될 경우의 처리 또한 진행되어야 한다.
    	- `GPIO.cleanup()` 이 현재는 **에러** 발생시 동작하지 않는다.
    - ~~따라서 `try-finally` 문을 이용하여 무조건 `finally` 절이 수행되도록 한다.~~ **적용완료**
2. ### [ex02_Btn_Polling.py](./ex02_Btn_Polling.py)
    - `GPIO` 핀을 **연결** 하여 `Button` 입력 받기
3. ### [ex03_Btn_Event.py](./ex03_Btn_Event.py)
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
7. ### [ex07_PWM_Servo.py](./ex07_PWM_Servo.py)
    - `Servo 모터` 를 활용한 실습
    - **Purse** 의 높이(Duty 비)가 모터의 **각도** 를 표현
    - 각도를 **입력**받아 `Servo모터` 조정
    - `Sevo 모터` 가 떨림 현상 발생
        - **Scheduling** 시간이 짧아 **jittering** 발생
8. ### [ex08_HC_SR04_Ultrasonic.py](./ex08_HC_SR04_Ultrasonic.py)
    - `초음파센서` 를 활용한 실습
9. ### [ex09_PIR.py](./ex09_PIR.py)
    - `PIR센서`를 활용한 실습
10. ### [ex10_MCP_3008.py](./ex10_MCP_3008.py)
    - **아날로그 입출력** 을 위해 `MCP_3008` 사용
    - `MISO`, `MOSI`, `SPICLK` 등 **SPI통신** 에서 사용한 것들을 이용하여 `아날로그 신호`를 다룬다.
    - `Timmy Diagram`
        - `xfer2([i1, i2, i3])`일때, **i1~i3** 는 `SCLK` 와 연관이 있다.
        - `i1` : start bit
        - `i2` : 하위 4bit는 don't care / 상위 1bit는 signal 선 , 나머지 3bit 는 채널
            - 하위 4bit가 `don't care` 이기 때문에 **<< 4** 가 진행
        - `i3` : don't care
        - `data` 출력의 경우 **(r[1] & 3) << 8 + r[2]** 와 같이 연산
        - **10bit** 의 해상도를 위해 **3** 만큼 비트마스킹