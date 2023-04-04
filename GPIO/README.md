# GATEWAY _ GPIO 📡
---
1. [ex01_LED_Blink.py](./ex01_LED_Blink.py)
	- `GPIO` 핀을 **연결** 하여 `LED` 조절
    - 현재는 입력되지 않았지만 **keyboard interrupt** 를 받게될 경우의 처리 또한 진행되어야 한다.
    	- `GPIO.cleanup()` 이 현재는 **에러** 발생시 동작하지 않는다.
    - ~~따라서 `try-finally` 문을 이용하여 무조건 `finally` 절이 수행되도록 한다.~~ **적용완료**
