import subprocess
import sys

zeroCount = 0
isPlaying = None

proc = subprocess.Popen(['parec', '--monitor-stream=513'],stdout=subprocess.PIPE)
# proc = subprocess.Popen(['echo', '"Foo"'],stdout=subprocess.PIPE)
while True:
    data = proc.stdout.read(1)
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
        # onPlayStateChange(newIsPlaying)
