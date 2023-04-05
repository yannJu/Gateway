# GATEWAY _ Rasberry Pi🎭
---
0. ### 라즈베리 파이 환경설정
	- `LCD` 연결
    - `Samba` 를 이용한 **공유 네트워크 폴더** 연결
    - `locale` 설정 (KO)

1. ### [GPIO(ex01_ex10)](./GPIO(ex01_ex10)/)
	- `GPIO` 를 이용하여 **입출력** 연습
    - `BCM` 모드를 통해 일반 **PIN** 번호가 아닌 `GPIO` 번호를 이용
    - **아두이노** 에서 사용한 센서들을 이용하여 간단한 실습 진행
2. ### [GPIO_ZERO(ex11_ex21)](./GPIO_ZERO(ex11_ex21))
    - `gpiozero` 라이브러리를 이용하여 보다 센서를 쉽게 다룰 수 있다.
3. ### [pigpio.py](./pigpio.py)
    - `jittering` 을 제어할 수 있다. → skeleton 코드는 메인 폴더에 *[pigpio.py](./pigpio.py)* 로 위치해 있다.
    
        ``` java
        $ sudo pigpiod
        ```
    - 터미널에 위의 명령어를 입력하여 `pigpiod` 서버를 실행
        - `pigpiod` 는 실제 **digital pin** 에 연결되어있는 서버 프로그램이다.
    - 해당 서버가 `PiGPIOFactory` 에 의해 **네트워크** 커넥션을 맺게된다.
    - 사용할 센서의 `pin_factory` 에 해당 커넥션 객체를 할당함으로써 센서의 핀을  `pigpiod`가 담당하게 된다.
4. ### [openCV(cv_ex01_cv_ex04)](./openCV(cv_ex01_cv_ex04)/)
    - `cv2`  모듈을 이용하여 간단한 실습
    - 라즈베리파이와 연동하여 **센서** 동작 함께 해보기