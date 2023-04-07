import cv2
from cv_ex10_harrdetect import HarrDetect

cap = cv2.VideoCapture(0)
harrXml = "haarcascade_frontalface_alt.xml"
harr = HarrDetect(harrXml)
blurRate = 15

while True:
    ret, frame = cap.read()
    if not ret: break
    
    faceLst = harr.detect(frame, (100, 100))
    frame = harr.draw_rect(frame, faceLst) # draw Rec
    
    #Blur ------
    # for (x, y, w, h) in faceLst:
    #     roi = frame[y:y + h, x:x + w]
    #     roi = cv2.resize(roi, (w // blurRate, h // blurRate))
    #     roi = cv2.resize(roi, (w, h))
    #     frame[y:y + h, x:x + w] = roi
        
    cv2.imshow("face Detect", frame)
    key = cv2.waitKey(25)
    
    if key == 27: break;
  
if cap.isOpened: cap.release()  
cv2.destroyAllWindows()