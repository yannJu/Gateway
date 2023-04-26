from datetime import datetime
import requests
from signal import pause


INTRUSION_URL = 'http://172.20.10.5:8000/iot/intrusion/'

def notify_instrusion():
    now = datetime.now()
    text = now.strftime("침입감지 . . . \n%Y-%m-%d %H:%M:%S")
    
    params = {
        'text' : text,
        'url' : 'http://172.20.10.5:8000/iot/mjpeg'
    }
    response = requests.get(INTRUSION_URL, params=params)
    res = response.json()
    
    if res['result'] == 'success': print("Detection Notified-!")
    else: 
        print("Detection Notify Fail. . .")
        print(res['reason'])
        
pir = motionSensor(21)
pir.when_motion = notify_instrusion
pause()