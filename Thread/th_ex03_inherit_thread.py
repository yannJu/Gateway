import threading, requests, time

class HtmlGetter(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self) #super().__init__() 시 self 안붙임
        self.url = url
        
    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        
        print(self.url, len(resp.text), "\n", resp.text)
        
url = "https://www.google.com"
thread = HtmlGetter(url)
thread.start()

thread.join()
print("END")