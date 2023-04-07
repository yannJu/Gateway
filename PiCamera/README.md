## PiCamera🗽
---
1. ### [pi_ex01_basic.py](./pi_ex01_basic.py)
   - `PiCamera` 모듈을 이용하여 **picamera** 활용
   - `start_preview()` 로 미리보기, `stop_preview()`로 미리보기 종료
      - `alpha` 를 조절하면 **투명도** 설정 가능
   - `rotation` 을 이용하면 이미지를 **회전** 시킬 수 있다.
2. ### [pi_ex02_capture.py](./pi_ex02_capture.py)
   - `resolution` 을 조절하여 **해상도** 설정 가능
   - `capture` 를 통해 **이미지** 를 저장할 수 있다.
      - 경로를 지정해주지 않으면 동일 경로에 저장된다.
3. ### [pi_ex03_continue_cap.py](./pi_ex03_continue_cap.py)
   - **5초** 간격으로 연속 촬영하기
   - `Text` 추가하기
      - `PiCamera` 모듈에서 **annotate_** 를 이용하여 지정 
      - `Color` 모듈에서 색상 지정
4. ### [pi_ex04_effect.py](./pi_ex04_effect.py)
   - 밝기(`brightness`), 대비(`contrast`) 조정가능
   - **효과** 를 설정해 줄 수 있다.
      - `PiCamera.IMAGE_EFFECTS` 에 들어있으며 원하는 **효과**를 `PiCamera.effect` 에 할당해준다.
5. ### [pi_ex05_video_record.py](./pi_ex05_video_record.py)
   - `start_recording` 을 이용하여 **동영상** 녹화
   - `h.264` 코덱으로 저장되는데 완전한 확장자가 아님 !
      - 확장자 명을 바꾸는 것으로 해결 안됨
      - `gpac` 패키지 설치
      
         ```sheel script 
            MP4 -add "기존파일" "변경파일"
         ```
      - 위와같이 쉘 명령 진행하여 변경
   - 혹은 파이썬에서 `subprocess` 라이브러리와 `os` 라이브러리를 활용해 쉘명령 진행 

   5-1) [video_util.py](./video_util.py) : **컨버터** 구현
6. ### [pi_ex06_motionSensor.py](./pi_ex06_motionSensor.py)
   - `MotionSensor` 와 함께 실습 진행
   - `Motion Sensor` 에 움직임이 감지되면 **녹화시작**
   - 감지 끝나면 **녹화 중단**
   - `opencv` 와 다르게 동시에 **스레드** 처리 되는 것이 아니므로 **상태변수** 를 줄 필요가 없다.
7. ### [pi_ex07_capture_io_bytes.py](./pi_ex07_capture_io_bytes.py)
   - **이미지 캡쳐(촬영)** 실습
   - 파일경로, 파일객체, IO.Bytes 스트림으로 저장할 수 있다.
      - 파일객체 : `f.open~` 과 같이 저장
      - IO.Bytes : 파일은 속도가 느리기 때문에 **스트림** 으로 저장 (메모리 파일)
   - `IO.Bytes` 를 기준으로 저장 → **파일객체** 로 캡쳐하는것과 크기는 크게 차이 나지 않는다.
      - 실제 파일로 저장하는지, 메모리 파일인지의 차이
8. ### [pi_ex08_capturePIL.py](./pi_ex08_capturePIL.py)
   - `seek()` : 시작, 현재, 끝 을 기준으로 되감기
   - 왜 `seek` 를 할까? 
      - **ptr** 이 파일의 **끝**에 있는 상태에서 `read` 하게 되면 **빈** stream 을 읽게 됨
   - 만약 **캡쳐** 후 다시 **write** 하게 되면 기존 캡쳐한 파일의 끝에 `ptr` 이 있기 때문에 그 이후에 **write** 하게된다.
      - **read** 할 방법이 없다.
      - `truncate` 를 이용하여 `ptr` 이후를 지운다. 
9. ### [pi_ex09_capture_sequence.py](./pi_ex09_capture_sequence.py)
   - `capture_sequence` 를 이용하여 연속 촬영하기
