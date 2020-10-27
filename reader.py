import subprocess
import sys

import react

def monitor(input, callback):
    zeroCount = 0
    isPlaying = None

    try:
        proc = subprocess.Popen(['parec', f"--monitor-stream={str(input['index'])}"], stdout=subprocess.PIPE)
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
                print(f"{input['name']}: {'playing' if newIsPlaying else 'not playing'}")
                isPlaying = newIsPlaying
                react.onPlayStateChange(newIsPlaying)
    except TypeError: # TypeError: ord() expected a character, but string of length 0 found
        callback(input, 'closed')

if __name__ == '__main__':
    print("I am… main.")
    monitor(513)
