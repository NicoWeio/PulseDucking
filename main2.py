# reads from `parec -d MySink.monitor | python3 main2.py`
import sys
import time

zeroCount = 0
isPlaying = None

while True:
    data = sys.stdin.buffer.read(1)
    isZero = ord(data) == 0
    newIsPlaying = isPlaying
    if (isZero):
        zeroCount += 1
    else:
        zeroCount = 0
        newIsPlaying = True
    if (zeroCount > 100):
        newIsPlaying = False

    if (newIsPlaying != isPlaying):
        print("playing" if newIsPlaying else "not playing")
        isPlaying = newIsPlaying

    #time.sleep(1)
        
print("END")
