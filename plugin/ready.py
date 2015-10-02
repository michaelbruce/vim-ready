import vim, sys, threading, time

global state
state = 'stop'


class Pomodoro(threading.Thread):
    def __init__(self):
        super(Pomodoro,self).__init__()
        self.daemon = True

    def run(self):
        time.sleep(10) # TODO this will change to 25 mins after testing
        while state != 'stop':
            print('started threaded after waiting 5 seconds')
            time.sleep(0.01)

if sys.argv[0] == 'ready':
    print("Let's go! Starting Pomodoro (25 minutes)")
    state = 'working'
    Pomodoro().start()
elif sys.argv[0] == 'stop':
    state = 'stop'
    print("Shutdown!")

