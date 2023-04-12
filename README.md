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
4. ### [openCV(cv_ex01_cv_ex15)](./openCV(cv_ex01_cv_ex15)/)
    - `cv2`  모듈을 이용하여 간단한 실습
    - `Video Capture` 부터, `Video Write` 등을 이용하여 이미지, 영상 처리
    - 라즈베리파이와 연동하여 **센서** 동작 함께 해보기
    - `harrdetect` 를 통해 **얼굴인식**
5. ### [PiCamera(pi_ex01_pi_ex10)](./PiCamera(pi_ex01_pi_ex10)/)
    - `PiCamera` 를 활용한 실습
    - 라즈베리파이에 연결하여 `Legacy` 를 설정해주어야한다.
        - `sudo raspi-config` 에 들어가 설정
    - **Python** 의 `Picamera` 모듈을 통해 실습 진행
6. ### [Thread(th_ex01_th_ex11)](./Thread(th_ex01_th_ex11)/)
    - `Process` : 실행중인 하나의 프로그램
        - 한 프로세스 내에서 여러개의 **스레드(thread)**를 동작 시킬 수 있다.
        - 프로세스마다 쓸 수 있는 **시간** 이 배정된다.
    - `Thread`
        - **메인 스레드** : 모든 프로그램은 **메인 스레드** 가 실행
            - 더이상 실행할 코드가 _**없는**_ 경우 종료
        - **작업 스레드** : **메인 스레드** 가 생성
            - **작업 스레드** 의 생성 유무는 `개발자` 의 선택사항 → 자동 생성 아님
    - `Process` 는 언제 **종료** 되는가?
        - **싱글** 인 경우 **메인 스레드** 종료와 동시에 종료
        - **멀티** 인 경우 모든 **스레드** 가 종료되어야 종료
    - **Python** 에서는 `threading` 이라는 모듈을 이용해서 스레딩 실행
        - `Thread` 클래스가 들어있음 . . 사용방법은 아래 _**두가지**_ 가 있다
            1. `Thread` 클래스에 실행할 **함수** 를 전달하여 실행
            2.  **상속** 을 사용하여 실행 → `run` 이라는 메소드를 꼭 **재정의** 
        * `start()` 를 실행해야 **작업 스레드** 로서 독립적으로 실행 된다.
7. ### [Audio](./Audio(au%2Ctts%2Csd)/)
    - `pyaudio` 를 이용하여 **녹음**, **저장**
    - `GoogleSpeech` 를 이용하여 **TTS**, **STT** 실습
    - `Sounddevice` 를 이용하여 **녹음**, **저장**
8. ### [Server](./Server/)
    - *[Server/NodeMCU_MQTT/](./Server/NodeMCU_MQTT/)* : `NodeMCU` 와`*MQTT` 를 통해 들어오는 데이터를 **서버** 에 전송
    - *[Server/NodeMCU_MQTT_v0.2/](./Server/NodeMCU_MQTT_v0.2/)* : 파일을 **서버**에 **업로드** 및 **다운로드**