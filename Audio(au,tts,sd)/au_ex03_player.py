import pyaudio
import wave
import sys

CHUNK = 1024
WAVE_FILENAME = "output.wav"

wf = wave.open(WAVE_FILENAME, 'rb')

audio = pyaudio.PyAudio()
stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()), 
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

data = wf.readframes(CHUNK) #buffer 크기 만큼 읽기

while data: #data 가 끝날때 까지 stream에 쓰고 buffer에 읽기를 반복
    stream.write(data)
    data = wf.readframes(CHUNK)
    
stream.stop_stream()
stream.close()

audio.terminate()