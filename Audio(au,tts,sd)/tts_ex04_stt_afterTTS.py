from io import BytesIO
from pydub import AudioSegment
from gtts import gTTS
import speech_recognition as sr

## TTS =====================
text = input("음성파일로 변환하기 위한 텍스트를 작성해주세요 @'.'@  (종료를 원한다면 exit 를 입력) >> ")

f = BytesIO()
tts = gTTS(text = text, lang = 'ko')
tts.save(f)

f.seek(0) #write 후 포인터가 이동하므로 읽기 위해서는 seek 사용
## ============================

## Convert mp32wav ==============
wav = BytesIO()
sound = AudioSegment.from_mp3(f)
sound.export(wav, format='wav')
wav.seek(0)
## =============================

## STT ==========================
r = sr.Recognizer()

with sr.AudioFile(wav) as w:
    audio = r.listen(w)
    print(r.recognize_google(audio, language='ko-KR'))
## ===================================