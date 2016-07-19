import time

from remote_control import Server


def print_cb(action):
    print(b'Received: ' + action)
    time.sleep(1)
    print(b'Done')
    return True


with Server(callback=print_cb) as server:
    server.run()
