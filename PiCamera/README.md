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
6. ### []()