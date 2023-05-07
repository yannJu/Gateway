import cv2
from gpiozero import  DistanceSensor
from time import sleep
from datetime import datetime
from fileUpload import upload
from makeDir import mkdir

isCap = 0
cap = cv2.VideoCapture(0)
upload_url = "http://172.20.10.5:8000/gateway/upload/"
dirPath = ""
fname = ""

def capture():
    global dirPath, fname, isCap
        
    cap.set(3, 640) # 너비
    cap.set(4, 480) # 높이
    startTime = datetime.now()
    
    dirPath = startTime.strftime('./data/%Y%m%d_%H_%M_%s')
    mkdir(dirPath)
    
    fname = startTime.strftime(f'{dirPath}/%Y%m%d_%H_%M_%s')

ultrasonic = DistanceSensor(16, 12)

# ultrasonic.when_in_range = capture
# ultrasonic.when_out_of_range = stop

cnt = 0
# ========CAPTURE =============
while True:    
    ret, frame = cap.read()
    if not ret: break
    
    if (isCap == 0):
        if (ultrasonic.distance * 100 < 30): 
            print(f"Detect ! //{ultrasonic.distance} cm//")
            isCap = 1
            capture()
        else: 
            sleep(0.1)
            continue
    
    now = datetime.now()
    txt = now.strftime("Capture . . %Y-%m-%d %H:%M:%S -- ")
    cv2.putText(frame, txt, (30, 30), cv2.FONT_ITALIC, 0.7, (180, 180, 0), 2, cv2.LINE_AA)
    cnt += 1
    
    cv2.imwrite(f'{fname}_{cnt}.jpg', frame) # 사진 저장
    print(f'[[ {fname}_{cnt}.jpg ]] SAVE -- ')
    
    if cnt == 6: 
        isCap = 0
        cnt = 0
        # ======UPLOAD =======
        for i in range(1, 7):
            upload(f'{fname}_{i}.jpg', upload_url)
            print(f'[[ {fname}_{i}.jpg ]] UPLOAD -- ')
            
        sleep(0.5)
    
    cv2.waitKey(333)