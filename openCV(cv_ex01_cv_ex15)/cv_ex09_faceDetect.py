from cv2.data import haarcascades
import cv2

cascade_file = "haarcascade_frontalface_alt.xml"
# print(haarcascades + "haarcascade_eye.xml") #경로 출력 가능

cascade = cv2.CascadeClassifier(cascade_file)

imgFile = "./data/face1.jpg"
img = cv2.imread(imgFile)
img_gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faceLst = cascade.detectMultiScale(img_gs, scaleFactor = 1.1, minNeighbors = 1, minSize = (150, 150))

if len(faceLst) > 0:
    print(faceLst)
    color = (0, 0, 255) #red
    for face in faceLst:
        x, y, w, h = face
        cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness=8)
        
    cv2.imwrite("faceDetect-output.PNG", img)
else: print("/NO/ Faces")