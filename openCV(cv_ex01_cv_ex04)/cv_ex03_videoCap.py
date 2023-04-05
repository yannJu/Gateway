import cv2

# cap = cv2.VideoCapture(0) # 0번 카메라
# cap = cv2.VideoCapture('./data/vtest.avi') # 로컬 비디오 파일
cap = cv2.VideoCapture('http://172.20.10.12:4747/video')
# 해상도 설정
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame Size = ', frame_size)

while True:
    ret, frame = cap.read()
    if not ret: break
    
    cv2.imshow('frame', frame)
    key = cv2.waitKey(25)
    if key == 27: break
if cap.isOpened():
    cap.release()
    
cv2.destroyAllWindows()