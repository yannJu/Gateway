import cv2
from cv_ex10_harrdetect import HarrDetect

# imgFile = "./data/face1.jpg"
imgSrc = "C:/Users/duswn/Pictures/Camera Roll/WIN_20221126_16_09_25_Pro.jpg"
imgFile = cv2.imread(imgSrc)
harrXml = "haarcascade_frontalface_alt.xml"

harr = HarrDetect(harrXml)
faceLst = harr.detect(imgFile)

blurRate = 5

for (x, y, w, h) in faceLst:
    face_img = imgFile[y: y + h, :x:x + w] #ROI
    face_img = cv2.resize(face_img, (w // blurRate, h // blurRate)) #축소
    
    face_img = cv2.resize(face_img, (w, h), interpolation = cv2.INTER_AREA) #재 확대
    
    imgFile[y:y + h, x:x + w] = face_img
    
cv2.imwrite("output_blur.PNG", imgFile)