#!/usr/bin/python3

import json
import threading
import time

import inputs
import reader

with open('config.json', 'r') as f:
    config = json.load(f)

watchingIndices = []

def onCallback(input, message):
    if message == 'closed':
        watchingIndices.remove(input['index'])
        print(f"Stopped watching {inputs.stringify(input)}")
    else:
        print("onCallback", input, message)

def updateWatches():
    inputsList = inputs.get()

    namesToWatch = [a['name'] for a in config['applications'] if a['role'] == 'master']

    inputsToWatch = [item for item in inputsList if item['name'] in namesToWatch]
    inputsToWatchNew = [i for i in inputsToWatch if i['index'] not in watchingIndices]

    for inputToWatch in inputsToWatchNew:
        print(f"Started watching {inputs.stringify(inputToWatch)}")
        t = threading.Thread(target=reader.monitor, args=[inputToWatch, onCallback])
        t.start()
        watchingIndices.append(inputToWatch['index'])

while True:
    updateWatches()
    time.sleep(config['preferences']['sourcesUpdateInterval'])
