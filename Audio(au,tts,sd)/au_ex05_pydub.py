from pydub import AudioSegment #데이터 처리
from pydub.playback import play #재생
from threading import Thread

def play(song):
    play(song)

song = AudioSegment.from_file('yanjo.wav', format='wav')
#song = AudioSegment.from_wav('test.wav')

# 아래와 같이 mp3 파일로 play 할 수 있다.
# song = AudioSegment.from_file('yanjo.mp3', format='mp3')
#song = AudioSegment.from_mp3('yanjo.mp3)

# play(song) #동기함수

work = Thread(taget=play, args = (song,))