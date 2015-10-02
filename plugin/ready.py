import vim, sys, threading, time

global state
state = 'stop'

# TODO count break whilst warning the user.
# TODO log pomodoros? (extension)
# TODO pyfile should work everywhere, not just locally.

class Pomodoro(threading.Thread):
    def __init__(self):
        super(Pomodoro,self).__init__()

    def run(self):
        time.sleep(10) # TODO this will change to 25 mins after testing
        while state != 'stop':
            print('started threaded after waiting 5 seconds')
            time.sleep(0.01)

if sys.argv[0] == 'ready':
    # TODO starting your first pomodoro of the day, change the message?
    print("Let's go! Starting Pomodoro (25 minutes)")
    state = 'working'
    Pomodoro().start()
elif sys.argv[0] == 'stop':
    state = 'stop'
    print("Shutdown!")

    # TODO keeping reminding every x seconds until python/prompt recieves the quitting input (like a snooze button)

