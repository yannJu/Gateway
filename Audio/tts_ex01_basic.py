from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

text = "나는 얀죠다 . ."

tts = gTTS(text=text, lang='ko')
tts.save('yanjo.mp3')

#파일 재생
media = AudioSegment.from_file('yanjo.mp3', format = 'mp3')
play(media)