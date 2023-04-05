from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host = 'localhost')
#이후 jittering 제어가 필요한 생성자의 끝에 pin_factory = factory 로 명시

#예시는 ex21