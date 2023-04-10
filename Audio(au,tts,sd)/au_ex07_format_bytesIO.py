from pydub import AudioSegment
from pydub.playback import play
import io
import requests

# 파일 읽기
with open('yanjo.wav', 'rb') as f:
    wavMem = io.BytesIO(f.read())
    
mp3Mem = io.BytesIO()
sound = AudioSegment.from_file(wavMem, format='wav')

#wav 파일을 BytesIO 를 이용하여 mp3로 변환
sound.export(mp3Mem, format = 'mp3', codec='libmp3lame')

print(mp3Mem.tell()) #file size print
mp3Mem.seek(0) #다시 작성할 수 있도록 포인터 이동

# 변환한 mp3 파일을 재생
song = AudioSegment.from_mp3(mp3Mem)
play(song)