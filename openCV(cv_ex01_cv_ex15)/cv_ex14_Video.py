import cv2
from time import sleep

class Video:
    def __init__(self, src): 
        self.cap = cv2.VideoCapture(src)
        
    def __iter__(self): # for문 객체
        return self
    
    def __next__(self): # for문의 다음 객체
        ret, image = self.cap.read()
        if ret: return image
        else: raise StopIteration
        
    def __enter__(self): # with 절 객체
        return self
    
    def __exit__(self, type, value, trace_back): # with 절 종료시 발생
        if self.cap and self.cap.isOpened(): 
            print("Video Release ===========")
            self.cap.release()
            cv2.destroyAllWindows()
            
    @staticmethod
    def show(img, exit_char = ord('q')):
        cv2.imshow("frame", img)
        if cv2.waitKey(1) & 0xFF == exit_char: return False
        
        return True
    
    @staticmethod
    def to_jpg(frame, quality=80):
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        is_success, jpg = cv2.imencode(".jpg", frame, encode_param)
        return jpg
    
    @staticmethod
    def resize_method(frame, width, height):
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
            
if __name__ == "__main__":
    video = Video(0)
    
    with video as v:
        for ix, img in enumerate(v):
            if ix == 5: break
            print(ix, img.shape)
            
            sleep(1)
    print("FIN")