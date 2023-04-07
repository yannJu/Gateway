import cv2
from cv_ex10_harrdetect import HarrDetect
from cv_ex14_Video import Video
from time import sleep

video = Video(0)
harrXml = "haarcascade_frontalface_alt.xml"
harr = HarrDetect(harrXml)
blurRate = 15
face_width = 200

with video as v:
    for ix, img in enumerate(v):
        faceLst = harr.detect(img, (70, 70))
        
        # 감지된 얼굴을 좌측 상단에 출력
        for (x, y, w, h) in faceLst:
            max_width = max(w, h)
            x = x + w // 2 - max_width // 2
            y = y + h // 2 - max_width // 2
            
            face_img = img[y:y + max_width, x:x + max_width].copy()
            face_img = video.resize_method(face_img, face_width, face_width)
            
            img[0:face_width, 0:face_width] = face_img[:]
        
        frame = harr.draw_rect(img, faceLst)
        video.show(frame)
        
print("FIN")