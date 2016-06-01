#!/usr/bin/env python

import os, sys
import threading, time

class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        self.do_something()

    def do_something(self):
        [i*i for i in range(1000)]
        time.sleep(1)

def main(args):
    threads = []
    for i in range(10):
        t = Worker()
        t.setDaemon(True)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main(sys.argv)
