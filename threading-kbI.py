#!/usr/bin/env python

import threading, Queue
import os, sys, time
import signal

class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            time.sleep(1)

class kbWatcher:
    def __init__(self):
        self.child = os.fork()
        if self.child == 0:
            return
        else:
            self.watch()

    def watch(self):
        try:
            os.wait()
        except KeyboardInterrupt:
            self.kill()
        sys.exit()

    def kill(self):
        try:
            os.kill(self.child, signal.SIGKILL)
        except OSError: pass

def main(args):
    threads = Queue.Queue(10)
    for i in range(10):
        t = Worker()
        t.setDaemon(True)
        threads.put(t)
        t.start()

    threads.join()

if __name__ == '__main__':
    kbWatcher()
    main(sys.argv)
