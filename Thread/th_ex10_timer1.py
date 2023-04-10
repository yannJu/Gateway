import threading

def do_something():
    print("Time out !")
    
timer = threading.Timer(2, do_something)
timer.start()
print("Main Thread Exit. .")