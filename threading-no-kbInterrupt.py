#!/usr/bin/env python

import os, sys
import threading, Queue
import time

class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        self.do_something()

    def do_something(self):
        [i*i for i in range(1000)]
        time.sleep(1)

def main(args):
    threads = Queue.Queue(10)
    for i in range(10):
        t = Worker()
        t.setDaemon(True)
        threads.put(t)
        t.start()

    threads.join()

if __name__ == '__main__':
    main(sys.argv)
