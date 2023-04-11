# SERVER💒
---
0. Tag 에는 `Gateway` 리포지토리 전체가 저장되어있기 때문에 . . . 버전은 **ZIP** 파일 내부에서 . . 구별가능 . . .
   - **README** 를 구별하기 위한 최선의 조치 ㅜ . ㅜ@@ 
1. ### NodeMCU 와 Django 연동
   - **Release** 에서 `MQTT_v0.1` 까지의 단계
   -   `NodeMCU` 를 통해 **조도 센서** 와 **온습도 센서**의 데이터를 받아온다.
   -   `Sensor`라는 모델을 생성하여 **서버** 에서 **Subscribe**
   -   **웹 브라우저** 와 연동하기 위해 `websocket` 통신 진행
   -   브라우저 `base.html` 등 추가 구현
2. ### 
   - **전등 켜기/끄기** 기능 추가(`Custom Switch`)
     -  전등의 유무에 따라 **Text 색상** 변경(`parentElement` 등을 통해 상위 클래스 접근) 