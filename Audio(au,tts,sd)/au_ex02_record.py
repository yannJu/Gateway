import pyaudio
import wave

CHUNK = 1024 #buffer size
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000

RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

audio = pyaudio.PyAudio()
stream = audio.open(input_device_index=3,
                    format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

#==============Recoding start
print("Start to record the audio !")
frames = []

for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK, exception_on_overflow=False) #데이터를 읽은 후
    frames.append(data) #저장
    
print("Recoding is Finished -")
# ==========================

stream.stop_stream()
stream.close()
audio.terminate()

# ==============save File
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf. setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()