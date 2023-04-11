## MQTT 서비스 연동(v0.2)🗻
---
→ **조도센서** 값 해결 @^.^@!
1. ### [Custom Switch 의 상태에 따른 LED Blink](./templates/iot/mqtt.html)
   - `Custom Switch` 를 이용하여 토글이 **on** 이면 `nodeMCU`의 내장 `led` 를 **on**, 토글이 **off** 면 `led` 도 **off** 하는 기능 구현

      ```html
        <div class="custom-control custom-switch" id='ledIcon'>
        <input type="checkbox" class="custom-control-input" id="ledcontrol">
        <label class="custom-control-label" for="ledcontrol">전등</label>
        </div>
      ```
    - `<div>` 태그에 **custom-switch** 클래스를 추가하고 하단에 **custom-control-. .** 을 추가해 준다.

      ![](../img/v2_img1.PNG)
    - 위와 같이 토글이 생성된 것을 볼 수 있다.
    - `<script>` 문 내에서 해당 토글 **Element**를 이용하여 동적처리를 해준다.

      ```java
       // 생략
        let ledcontrol = document.getElementById('ledcontrol');
       // . . 중략
       // 전등 제어
        ledcontrol.onclick = () => {
          // console.log(ledcontrol.checked);
          const topic = "iot/control/led";
          let msg;

          if (ledcontrol.checked) msg = "on";
          else msg = "off";
          
          const message = new Paho.MQTT.Message(msg);
          message.destinationName = topic;
          message.qos = 1;
          
          client.send(message);
        }
      ```
    - **true** 값이 들어오면 **on**을, **false** 값이 들어오면 **off** 를 `publish` 하도록 구현하였다.
2. 