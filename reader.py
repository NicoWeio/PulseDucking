import subprocess

def monitor(input, supervisor):
    zeroCount = 0
    isPlaying = None

    try:
        # TODO: read stderr instead of redirecting to DEVNULL
        proc = subprocess.Popen(['parec', f"--monitor-stream={str(input.index)}"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
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
                print(f"{input}: {'playing' if newIsPlaying else 'not playing'}")
                isPlaying = newIsPlaying
                supervisor.onPlayStateChange(newIsPlaying)

    except TypeError: # TypeError: ord() expected a character, but string of length 0 found
        supervisor.onClose(input)
