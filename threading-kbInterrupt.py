#!/usr/bin/env python

import os, sys
import threading, time

class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.kill_received = False

    def run(self):
        while not self.kill_received:
            self.do_something()

    def do_something(self):
        [ i*i for i in range(1000) ]
        time.sleep(1)

def main(args):
    threads = []
    for i in range(10):
        t = Worker()
        threads.append(t)
        t.start()

    while len(threads) > 0:
        try:
            threads = [t.join(1) for t in threads if t is not None and t.isAlive()]
        except KeyboardInterrupt:
            print('Ctrl-c received.')
            for t in threads:
                t.kill_received = True

if __name__ == '__main__':
    main(sys.argv)
