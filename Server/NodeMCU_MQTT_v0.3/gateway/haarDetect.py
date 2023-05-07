import cv2
from cv2.data import haarcascades
import os

class HarrDetect:
    def __init__(self, cascade_file):
        harr_xml = os.path.join(haarcascades, cascade_file)
        self.cascade = cv2.CascadeClassifier(harr_xml)
        
    def detect(self, img, minSize = (150, 150)):
        imgGs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faceLst = self.cascade.detectMultiScale(imgGs, scaleFactor = 1.1, minNeighbors = 1, minSize = minSize)
        
        return faceLst
    
    def draw_rect(self, img, faceLst, color = (0, 0, 255), thickness = 8):
        for face in faceLst:
            x, y, w, h = face
            cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)
            
        return img