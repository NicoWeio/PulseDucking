import subprocess

def get():
    def reset():
        index = None
        state = None
        name = None

    reset()
    devices = list()

    stdoutdata = subprocess.getoutput("pacmd list-sink-inputs")
    # print(stdoutdata)

    for line in stdoutdata.splitlines()[1:]:
        if 'index' in line:
            index = line.split(': ')[1]
        elif 'state: ' in line:
            state = line.split(': ')[1]
        elif 'application.name = ' in line:
            name = line.split(' = "')[1][:-1]
            devices.append({
            'index': index,
            'state': state,
            'name': name,
            })
            reset()

    return devices

def stringify(input):
    return f"{input['name']} ({input['index']})"

if __name__ == '__main__':
    print("I am… main.")
    print(get())
