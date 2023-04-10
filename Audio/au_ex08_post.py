import requests
import io

mp3Mem = io.BytesIO()
mp3Mem.seek(0)

upload = {'file' : ('yanjo.mp3, mp3Mem')}

res = requests.post('http://127.0.0.1:8000/test', files = upload)