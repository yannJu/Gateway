# SERVER💒
---
0. ### [nodeMCU_esp/](./nodeMCU_esp/)
   - `Django` 와 연동할 `nodeMCU` 코드 폴더 
1. ### [NodeMCU 와 Django 연동(MQTT_v0.1)](./NodeMCU_MQTT/)
   - **Release** 에서 `MQTT_v0.1` 까지의 단계
   -   `NodeMCU` 를 통해 **조도 센서** 와 **온습도 센서**의 데이터를 받아온다.
   -   `Sensor`라는 모델을 생성하여 **서버** 에서 **Subscribe**
   -   **웹 브라우저** 와 연동하기 위해 `websocket` 통신 진행
   -   브라우저 `base.html` 등 추가 구현
2. ### [](./NodeMCU_MQTT_v0.2/)
   - **전등 켜기/끄기** 기능 추가(`Custom Switch`)
   - 