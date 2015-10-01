import vim, sys, threading, time

class Pomodoro(threading.Thread):
    def __init__(self):
        super(Pomodoro,self).__init__()

    def run(self):
        time.sleep(5)
        print('started threaded after waiting 5 seconds')

if sys.argv[0] == 'ready':
    # TODO starting your first pomodoro of the day, change the message?
    print("Let's go! Starting Pomodoro (25 minutes)")
    Pomodoro().start()

    # TODO keeping reminding every x seconds until python/prompt recieves the quitting input (like a snooze button)

