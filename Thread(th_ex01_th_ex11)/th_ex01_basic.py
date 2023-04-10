import threading

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
        
    print('SubThread ', total)
    
t = threading.Thread(target=sum, args=(1, 100000)) 
t.start() # 꼭 작성해야한다

print("Main Thread")