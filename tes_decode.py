#!/usr/bin/env python
# encoding=utf-8

a = {'一':'张', '二':'王', '三':'李', '四':'赵'}
b = '一'

for key, value in a.iteritems():
    print key, value

print('%s' % a[b].decode('utf-8'))
