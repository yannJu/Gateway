import cv2

cap = cv2.VideoCapture(0)
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print('frame_size : ', frame_size)

fourcc = cv2.VideoWriter_fourcc(*'mp4v') # '*' 펼침 연산자를 이용하여 (m,p,4,v) 로 전달

out1 = cv2.VideoWriter('./data/recored0.mp4', fourcc, 20.0, frame_size)
out2 = cv2.VideoWriter('./data/recored1.mp4', fourcc, 20.0, frame_size, isColor = False)

while True:
    ret, frame = cap.read()
    if not ret: break
    
    out1.write(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out2.write(gray)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    key = cv2.waitKey(25)
    if key == 27: break
    
cap.release()
out1.release()
out2.release()

cv2.destroyAllWindows()