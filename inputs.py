#!/usr/bin/python3

import subprocess

class Input:
    def __init__(self, index, name, state):
        self.index = index
        self.name = name
        self.state = state
    def __str__(self):
     return f"{self.name} ({self.index})"

def get():
    def reset():
        index = None
        state = None
        name = None

    reset()
    devices = list()

    data = subprocess.getoutput("pacmd list-sink-inputs")
    # print(data)

    for line in data.splitlines()[1:]:
        if 'index' in line:
            index = line.split(': ')[1]
        elif 'state: ' in line:
            state = line.split(': ')[1]
        elif 'application.name = ' in line:
            name = line.split(' = "')[1][:-1]
            devices.append(Input(index, name, state))
            reset()

    return devices

if __name__ == '__main__':
    print(get())
