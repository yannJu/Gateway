import io
import queue
import sounddevice as sd
import soundfile as sf
import sys

samplerate = 44100
channels = 1

sd.default.samplerate = samplerate
sd.default.channels = channels

q = queue.Queue()
recMem = io.BytesIO()

#Producer, 녹음 스레드가 하는 일
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy()) 
    
try:
    with sf.SoundFile(recMem, mode='x', format='wav',
                      samplerate=samplerate, channels=channels) as f:
        with sd.InputStream(callback=callback):
            print("#" * 80)
            print('Press \"Ctrl + C\" to stop the Recoring-')
            print("#" * 80)
            # Producer, 실질적으로 Main Thread 가 하는일
            while True:
                f.write(q.get())
                
except KeyboardInterrupt:
    print(recMem.tell())
    print("\nRecoring Finished : ")
except Exception as e:
    print(e)