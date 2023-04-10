## Audio🌂
---
### Pydub 등을 이용한 Audio 실습
1. ### [au_ex01_selectMic.py](./au_ex01_selectMic.py)
   - `Audio` 장치를 찾기위한 **정보** 출력
2. ### [au_ex02_record.py](./au_ex02_record.py)
   - **채널**이 1개 라면 `mono`, 2개 이상이면 `stereo`
   - 1개 측정해서 **digital** 로 변환하려는 포맷 지정
     - `Volume Level` 을 의미한다.
     - bit가 커질수록 범위가 넓어지므로
   - 1초에 몇번 측정할거냐를 제어 → `Rate`
     - **44100** 은 보통 `CD`음질
     - `CD`의 절반정도는 `라디오` 음질 . .
   - Q. 1초에 생성되는 데이터의 크기는?
     - 1회 **Sampling** 크기는 2Byte
     - 1회 **Sampling** 횟수는 48000
     - 1개의 채널 
     - 2Byte * 48000 * 1 = **96K(96,000Byte)**
   - `Chunk` : 미리 메모리를 확보, **Buffer** 의 크기
   - **wave** 모듈은 `wave` 파일로 저장하기 위해 필요하다.
3. ### [au_ex03_player.py](./au_ex03_player.py)
   - **데이터**를 읽어올 때에도 **Sampling** 크기, 횟수, 채널이 필요하다.
     - `getchannels()`, `getframerate()`, `getsampwidth()`  을 이용
4. ### [au_ex04_audio_withThread.py](./au_ex04_audio_withThread.py)
   - `Thread` 를 이용하여 녹음 실습
   - 프로그램이 시작하면 **녹음시작**
   - `Enter` 가 입력되면 **녹음중단**
   - 이후 **파일명** 입력받기
   - 파일 저장
   - `stream` 을 `close` 하면 세그멘테이션 에러가 난다 . . 왜일까 . .
5. ### [au_ex05_pydub.py](./au_ex05_pydub.py)
   - `AudioSegment` 를 이용하여 **데이터 처리**
   - `play` 를 이용하여 **재생**
      - 이때 `play` 는 동기함수
   - **Thread** 화도 가능
6. ### [au_ex06_format.py](./au_ex06_format.py)
   - 파일 **포맷** 변환
   - `ffmpeg` 를 이용하여 변환한다.
   - **codec** 명을 입력하여 `wav` 에서 `mp3` 파일로 변환할 수 있다.
7. ### [au_ex07_format_bytesIO.py](./au_ex07_format_bytesIO.py)
   - `frame` 을 읽는 것은 오래걸리기 때문에 **BytesIO** 사용
   - 다른 차이점 없이 **파일명** 에서 **BytesIO** 객체로만 변경하면 된다.
   - `tell()` : 현재 파일 포인터(**ptr**) 의 위치를 알려준다.
      - _**파일 크기**_ 를 구할 수 있다.
8. ### [au_ex08_post.py](./au_ex08_post.py)
   - `POST` 메소드를 이용하여 녹음된 파일을 **서버**로 `Upload` 가능
   - `json` 타입으로 전송
   - `Bucket3` 에 파일을 담아서 보내게 되면 **클라우드** 에도 전송이 가능
     - `Bucket` 에 파일이 업로드 되면 클라우드로 보낼 수 있도록 **AWS SDK** 를 조정하면 된다 . .! 
      - 이건 클라우드 하는 분들 께 여쭤보ㅈ ㅏ ..
---
### Google Speech 를 이용한 실습
1. ### [tts_ex01_basic.py](./tts_ex01_basic.py)
   - `gtts` 라이브러리를 이용하여 작성한 **텍스트** 를 음성변환
   - 앞서 실습한 내용을 바탕으로 `play`
2. ### [tts_ex02_stt.py](./tts_ex02_stt.py)
   - **음성**파일을 `speechRecognition` 을 통해 **텍스트** 로 변환
3. ### []()
   - 굳이 **실제 파일** 을 가지고 데이터를 처리할 필요가 없다.
   - `BytesIO` 를 이용하여 **데이터 가공**하고자 하는데 지원을 하는지 확인
     - 하지만 **tts** 는 `BytesIO` 를 지원하지 않는다.
     - 오픈소스를 수정하여 `BytesIO`를 지원 가능하도록 수정 . . !