#/usr/bin/env python
# -*- coding=utf-8 -*-

# Get 100 items every time from a large list(dont know length)

import sys

a_large_list = range(0, 1989)

a_large_list_gen = (x for x in a_large_list)

while True:
    for i in range(0, 100):
        try:
            print(a_large_list_gen.next()),
        except StopIteration:
            sys.exit()
    print('\n')
