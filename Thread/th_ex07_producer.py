from threading import Thread
import random
import time

class Producer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.setDaemon(True)
        self.queue = queue
        self.count = 0
        
    def produce(self):
        delay = random.uniform(0.5, 3)
        time.sleep(delay)
        
        self.count += 1
        msg = self.count
        print('Producer prodce : ', msg)
        self.queue.put(msg)
        
    def run(self):
        while True:
            self.produce()