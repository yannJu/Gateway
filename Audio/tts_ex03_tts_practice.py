from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS

while True:
    text = input("음성파일로 변환하기 위한 텍스트를 작성해주세요 @'.'@  (종료를 원한다면 exit 를 입력) >> ")
    if text == 'exit': break
    
    f = BytesIO()
    tts = gTTS(text = text, lang = 'ko')
    tts.save(f)
    
    f.seek(0) #write 후 포인터가 이동하므로 읽기 위해서는 seek 사용
    
    song = AudioSegment.from_mp3(f) #BytesIO 로 읽어오기
    song.export('convert_yanjo.mp3', format='mp3', codec='libmp3lame')
    # play(song)