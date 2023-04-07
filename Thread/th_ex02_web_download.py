from threading import Thread
import requests
import time

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    
    print(url, len(resp.text), resp.text)
    
url = "https://www.naver.com"
thread = Thread(target=getHtml, args=(url, ))
thread.start()

print("Main Thread")