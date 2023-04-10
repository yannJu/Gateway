import sounddevice as sd

duration = 5.5

def callback(indata, outdata, frames, time, status):
    # 실제데이터, 출력데이터, 몇번째 데이터인지에 대한 설명, 시간, 상태(오류가 있는지 없는지 . . 일반적으로는 0 )
    
    if status: print(status)
    outdata[:] = indata
    
with sd.Stream(channels=1, callback=callback):
    #몇번 장치를 사용할지 지정하지 않은 경우 default 로 체크된 것을 사용
    sd.sleep(int(duration * 1000))