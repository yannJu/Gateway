## OPENCV🥼
---
0. ### [ex00_showVideo.py](./ex00_showVideo.py)
   - **ex03** 에 계속 비디오 변수를 만들기 번거로워서, `input` 을 통해 경로를 받도록 구현
1. ### [cv_ex01_imread_imshow.py](./cv_ex01_imread_imshow.py)
   - `cv2` 를 이용하여 `imread` 를 통해 **이미지** 를 읽어오고 `imshow` 를 통해 띄우기 
2. ### [cv_ex02_saveImg.py](./cv_ex02_saveImg.py)
   - `imwrite` 를 통해 파일 저장
   - 서버에 **이미지** 를 업로드 할 경우 `파일 크기` 를 신경 써야한다.
   - **이미지의 크기** 등을 조정하여 `파일을 축소` 하는 등 조정이 필요하다.
3. ### [cv_ex03_videoCap.py](./cv_ex03_videoCap.py) 
   - `VideoCapture` 를 이용하여 카메라 센서와 연결
     - **카메라 센서** 와 연결할 수도 있지만 경로를 입력하면 **로컬 비디오 파일** 실행이 가능
     - `DroidCam` 을 이용하여 **ip카메라** 와도 연결이 가능 → **url** 입력 (`MJpeg` 스트림 : *[cam.html](./cam.html)* 처럼 스트림 가능)
   -  `cap.read()` 의 경우 제대로 이미지가 들어왔는지의 **여부**와 **frame** 이 들어오게 된다.
   -  `waitKey()` 에 따라 **fps**  조절이 가능
      -  `waitKey(25)` 라면 25ms 를 기다리기 때문에 1000 / 25 = 40 으로 **40fps**가 된다.
4. ### [cv_ex04_videoWrite.py](./cv_ex04_videoWrite.py)
    - `VideoWriter` 를 이용하여 비디오 녹화
    - `*` 를 이용하여 펼침 연산자 활용
    - `BGR2GRAY` 를 통해 흑백 이미지로 변환
5. ### [cv_ex05_putText_videoRW.py](./cv_ex05_putText_videoRW.py)
   - `putText` 를 이용하여 **이미지** 에 **text** 추가
   - `video cam` 에서 비디오를 입력받고 **text** 를 추가하여 `video write` 
6. ### [cv_ex06_ROI1.py](./cv_ex06_ROI1.py)
   - 이미지를 **슬라이싱**을 이용하여 `관심영역(ROI)` 추출
   - `numpy` 에서는 **[y, x]** 로, `opencv` 에서는 **(x, y)** 로 읽음
7. ### [cv_ex07_ROI2_Blur.py](./cv_ex07_ROI2_Blur.py)
   - 주어진 **이미지** 를 연산을 이용하여 `Blur` 처리 되는 코드 구현
8. ### [cv_ex08_MotionSensor_withVideoWrite.py](./cv_ex08_MotionSensor_withVideoWrite.py)
   - `MotionSensor` 에 움직임이 감지되면 `Video Capture`를 시작
   - 움직임이 더이상 감지 되지 않으면 `Recording` 중단
   - 이때, `release()` 와 `putText()` 가 동시에 동작하기 때문에 **상태변수** 를 지정하여 구현하여야 한다. 