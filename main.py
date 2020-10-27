#!/usr/bin/python3

import json
import threading
import time

import inputs
import react
import reader

with open('config.json', 'r') as f:
    config = json.load(f)

watchingIndices = []

class Supervisor:
    def onPlayStateChange(self, playing):
        react.onPlayStateChange(playing)
    def onClose(self, input):
        watchingIndices.remove(input['index'])
        print(f"Stopped watching {inputs.stringify(input)}")

supervisorInstance = Supervisor()

def updateWatches():
    inputsList = inputs.get()

    namesToWatch = [a['name'] for a in config['applications'] if a['role'] == 'master']

    inputsToWatch = [i for i in inputsList if i['name'] in namesToWatch]
    inputsToWatchNew = [i for i in inputsToWatch if i['index'] not in watchingIndices]

    for inputToWatch in inputsToWatchNew:
        print(f"Started watching {inputs.stringify(inputToWatch)}")
        t = threading.Thread(target=reader.monitor, args=[inputToWatch, supervisorInstance])
        t.start()
        watchingIndices.append(inputToWatch['index'])

while True:
    updateWatches()
    time.sleep(config['preferences']['sourcesUpdateInterval'])
