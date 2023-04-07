import cv2

source = input("비디오의 경로를 작성해주세요 >> ")

cap = cv2.VideoCapture(source)

while True:
    ret, frame = cap.read()
    if not ret: break
    
    cv2.imshow("frame", frame)
    key = cv2.waitKey(50)

    if key == 27: break

cap.release()
cv2.destroyAllWindows()
