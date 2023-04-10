from pydub import AudioSegment
from pydub.playback import play

#wav2mp3
sound = AudioSegment.from_file('yanjo.wav', format='wav')
sound.export('convert_yanjo.mp3', format='mp3', codec='libmp3lame')

#mp32wav
sound = AudioSegment.from_file('convert_yanjo.mp3', format='mp3')
sound.export('convert_yanjo.wav', format='wav')