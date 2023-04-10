# producer  와 consumer 가 서로 속도가 다르다고 가정
# producer 가 속도가 더 빠르다면 Queue 가 꽉 차게 된다.
# consumer 가 빠르다면 Queue 가 비게 된다.
# 이때 Queue는 공유자원이다.
# 따라서 동기화 Queue 를 사용한다. 
# Start 호출 후 다시 Start 할 수 없다. . 다시 하고 싶다면 cancel() 후 다시 Start()
from threading import Thread
import random
import time

class Consumer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.setDaemon(True)
        self.queue = queue
        
    def do(self, msg):
        print('Consumer do : ', msg)
        delay = random.uniform(0.5, 3)
        time.sleep(delay)
        
    def run(self):
        while True:
            msg = self.queue.get()
            self.do(msg)