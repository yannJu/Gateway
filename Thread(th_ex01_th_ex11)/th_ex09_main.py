import time
from consumer import Consumer
from producer import Producer
from queue import Queue

def main():
    q = Queue(5)
    
    c = Consumer(q)
    p = Producer(q)
    
    c.start()
    p.start()
    
    time.sleep(10)
    
main()