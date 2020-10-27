#!/usr/bin/python3

import threading
import time

import reader
import get_inputs

try:
    inputs = get_inputs.get()
    # print(inputs)

    inputsToWatch = (item for item in inputs if item['name'] == 'Google Chrome')
    inputToWatch = next(inputsToWatch, None)
    print(list(inputsToWatch))
    if inputToWatch:
        print(f"Watching{inputToWatch['name']} ({inputToWatch['index']})")
        t = threading.Thread(target=reader.monitor, args=[inputToWatch['index']])
        t.start()
    else:
        print("Nothing to watch.")
        # exit()

except:
   print ("Error: unable to start thread (???)")
