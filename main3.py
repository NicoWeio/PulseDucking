import time as time
import signal

#Close session
def handler(signum, frame):
    print 1
    raise Exception('Action took too much time')


signal.signal(signal.SIGALRM, handler)
signal.alarm(3) #Set the parameter to the amount of seconds you want to wait

try:
   #TODO

    for i in range(0,5):
        time.sleep(1)
except:
    print 2

signal.alarm(10) #Resets the alarm to 10 new seconds
signal.alarm(0) #Disables the alarm 
