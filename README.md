# PulseDucking

Have you ever wanted to listen to music while hanging out in a voice chat, but you couldn't understand your friends because the music was too loud, or you couldn't enjoy the music because you had to lower its volume so much? Does it annoy you to manually stop Spotify every time you play a video? (WIP)
Fear no more, because PulseDucking could be exactly what you want!

PulseDucking lowers the volume of your music (/…), whenever your voice chat (/…) becomes noisy.

## Features

-   Detect **silence**, not **presence of an audio source** or **playback status**. Discord, for example, won't close its audio output or update playback state when nobody is talking.
-   **Easy customization** via a JSON config file.

## Requirements

-   Python 3
-   PulseAudio

## About the competition

_PulseAudio_ ships with a module called [**module-role-ducking**](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/#module-role-ducking). It has an important problem, though:
The software you use has to set their _media.role_ property, so that _module-role-ducking_ can identify whether it should trigger ducking or be ducked. Some do it – others don't.

[**Mumble**](https://wiki.mumble.info/wiki/Features#Attenuation) has ducking built in. They call it _Attenuation_. That's only for Mumble, though.

[**Android**](https://developer.android.com/guide/topics/media-apps/audio-focus) is a good example for audio ducking. You may have noticed that while Google Maps tells you the next direction, the volume of your music is reduced. Or when you start a YouTube video, the music you were playing is paused. But you don't use Android on your PC, do you?

## How it's done

- For each currently running _trigger_ application, a new thread is started.
- In each thread, `parec --monitor-stream=<STREAM_INDEX>` is called. It streams the raw audio of an application.
- By simply checking for `0x00`, silence/noise is detected.
- `pacmd set-sink-input-volume <SINK_INPUT_INDEX> <VOLUME>` is dispatched for all _ducking_ applications.
- A loop ensures that new applications are taken into account as well.
