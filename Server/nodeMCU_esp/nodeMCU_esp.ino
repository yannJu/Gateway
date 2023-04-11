#include <MqttCom.h>
#include <DHT.h>
#include <Analog.h>
#include <LED.h>

MqttCom com;

LED led(BUILTIN_LED);

const char *ssid = "ㅇㅇㅈㅇ ㅇㅇㅍ";
const char *pwd = "2duswn!!";
const char *mqtt_server = "172.20.10.5";

int value = 0;

Analog cds(A0, 100, 0);
DHT dht11(D7, DHT11);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  com.init(ssid, pwd);
  com.setServer(mqtt_server, "iot/control/led", callback);
  // com.setServer(mqtt_server, NULL, callback); //inTopic 으로 subscribe 도 함
  com.setInterval(15000, publish); //2초마다 publish

  dht11.begin();
}

void loop() {
  // put your main code here, to run repeatedly: 
  com.run();
}

void publish() {
  float illu, humi, temp;

  illu = cds.read();
  humi = dht11.readHumidity();
  temp = dht11.readTemperature();

  Serial.print("Illu : ");
  Serial.println(illu);
  
  Serial.print("Temp : ");
  Serial.println(temp);
  
  Serial.print("Humi : ");
  Serial.println(humi);

  com.print(0, "T:", temp, " H:", humi);
  com.print(1, "I:", illu);

  //publish 
  com.publish("iot/yanjo/sensor/livingroom/illuminate", illu);
  com.publish("iot/yanjo/sensor/bedroom/temperature", temp);
  com.publish("iot/yanjo/sensor/kitchen/humidity", humi);
}

void callback(char *topic, byte *payload, unsigned int length) {
  char buf[128];
  memcpy(buf, payload, length);
  buf[length] = '\0';

  String msg = buf;
  if (msg == "on") led.setValue(0);
  else led.setValue(1);
}