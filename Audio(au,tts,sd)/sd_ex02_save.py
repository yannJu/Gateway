import sounddevice as sd
import soundfile as sf

fs = 44100 #sample rate
seconds = 3 #Duration recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait() #wait until recording is finished

sf.write('yanjo.wav', myrecording, fs)