from cv_ex10_harrdetect import HarrDetect
import cv2

# imgFile = "./data/face1.jpg"
imgSrc = "C:/Users/duswn/Pictures/Camera Roll/WIN_20221126_16_09_25_Pro.jpg"
imgFile = cv2.imread(imgSrc)
harrXml = "haarcascade_frontalface_alt.xml"

harr = HarrDetect(harrXml)
faceLst = harr.detect(imgFile)

getDetect = harr.draw_rect(imgFile, faceLst)
if (len(getDetect) > 0): cv2.imwrite("faceDetect-output.PNG", getDetect)
else: print("/No/ Detect-")