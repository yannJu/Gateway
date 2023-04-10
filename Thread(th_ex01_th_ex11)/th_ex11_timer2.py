import threading
from time import sleep

def do_something():
    print('Time out - !')
    
timer = threading.Timer(2, do_something)
timer.start()

sleep(1)

timer.cancel() # 1초 쉬고 sleep 했기 때문에 2초 안넘어서 . . . . 출력안됌
# restart 를 원한다면 다시 "생성" 시켜서 Start
timer = threading.Timer(2, do_something)
timer.start()