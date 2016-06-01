#!/usr/bin/env python
# -*- coding=utf-8 -*-

import threading
import time, sys

class TimeLoop(object):
    '''
    间隔一定时间循环执行程序
    '''

    def loop(self):
        def sayhello():
            print('Hello', time.ctime())
            
            global t
            t = threading.Timer(5.0, sayhello)
            t.start()

        t = threading.Timer(2.0, sayhello)
        t.start()

if __name__ == '__main__':
    keWatcher()
    test = TimeLoop()
    test.loop()
    print('It works.')
