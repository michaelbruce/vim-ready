import vim, sys, threading, time

# def python_input(message = 'input'):
#   vim.command('call inputsave()')
#   vim.command("let user_input = input('" + message + ": ')")
#   vim.command('call inputrestore()')
#   return vim.eval('user_input')

global state
state = 'stopped'

# TODO count break whilst warning the user.
# TODO log pomodoros? (extension)
# TODO pyfile should work everywhere, not just locally.

class Pomodoro(threading.Thread):
    def __init__(self):
        super(Pomodoro,self).__init__()

    def run(self):
        time.sleep(5) # TODO this will change to 25 mins after testing
        while state != 'stopped':
            print('started threaded after waiting 5 seconds')
            time.sleep(1)

if sys.argv[0] == 'ready':
    # TODO starting your first pomodoro of the day, change the message?
    print("Let's go! Starting Pomodoro (25 minutes)")
    state = 'working'
    Pomodoro().start()
elif sys.argv[0] == 'stop':
    state = 'stopped'

    # TODO keeping reminding every x seconds until python/prompt recieves the quitting input (like a snooze button)

