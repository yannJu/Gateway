import spidev
import time

delay = 0.5

# mCP3008 채널 중 센서에 연결한 채널 설정
pot_channel = 0

spi = spidev.SpiDev()
spi.open(0, 0)

spi.max_speed_hz = 100000

def readadc(adcnum):
    if adcnum < 0 or adcnum > 7: return -1
    
    r = spi.xfer2([1, 8 + adcnum <<4, 0])
    print(r)
    data = ((r[1] & 3) << 8) + r[2]
    
    return data

while True:
    pot_value = readadc(pot_channel)
    print("---------------------------------")
    print("LDR value : ", pot_value)
    
    time.sleep(delay)