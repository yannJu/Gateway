import speech_recognition as sr

r = sr.Recognizer()

# with sr.Michropone() as src:
with sr.AudioFile('./media/yanjo.wav') as src:
    audio = r.listen(src)
    print(r.recognize_google(audio, language = 'ko-KR'))