import math
import subprocess

duckPercent = 30
FULL_VOLUME = 65536

def onPlayStateChange(playing):
    # print(subprocess.check_output(['dbus-send', '--print-reply', '--dest=org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2', 'org.mpris.MediaPlayer2.Player.' + ('Play' if not playing else 'Pause')]))
    volume = math.floor(FULL_VOLUME * ((100-duckPercent) / 100)) if playing else FULL_VOLUME
    r = subprocess.check_output(['pacmd', 'set-sink-input-volume', '513', str(volume)])
