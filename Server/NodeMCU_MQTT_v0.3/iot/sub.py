import paho.mqtt.client as mqtt
from .models import Sensor
from django.utils import timezone
from django.conf import settings

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    if rc == 0:
        print("MQTT 브로커 연결 성공, iot/# 구독 신청 @.@  . .")
        client.subscribe("iot/yanjo/sensor/#") #iot/sensor 하위 토픽 전체 subscribe
    else: print("연결 실패 : ", rc)
    
def on_message(client, userdata, msg):
    value = int(msg.payload.decode()) #byte 배열을 str으로 변환
    if settings.MQTT_DEBUG_PRINT: print(f" {msg.topic} {value} ")
    _, _, _, place, category = msg.topic.split('/') 
    
    #DB 저장
    data = Sensor(place = place, category = category, value = value, created_at = timezone.now())
    data.save()
    
if (settings.MQTT_SUBSCRIBE):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect('localhost')
        client.loop_start() #새로운 스레드(daemon)
    except Exception as err:
        print(f"Err ! /{err}/")