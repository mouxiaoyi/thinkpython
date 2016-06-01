#!/usr/bin/env python
# -*- coding=utf-8 -*-

# modify the content before login the system. this example show the hostname,interface/ip/mac.
# excute this script in /etc/rc.local while bootup.
# 

import sys, commands

sys.stdout = open('/etc/issue', 'write')

HOSTNAME = commands.getoutput('hostname')
print('Welcome to %s.' % HOSTNAME )

interfaces = commands.getoutput('cat /proc/net/dev').split('\n')

# find the interface like eth0, eth1, lo etc.
ports = []
for interface in interfaces:
    interface = interface.strip()
    if ':' in interface:
        ports.append(interface.split(':')[0])

print('Local ip info:')
for port in ports:
    ipcmd = "ifconfig " + port + " | sed -e '/.*inet addr:/!d;s///;s/ .*//'"
    ipaddr = commands.getoutput( ipcmd )

    maccmd = "ifconfig " + port + " | sed -n '/HWaddr/ s/^.*HWaddr *//pg'"
    macaddr = commands.getoutput( maccmd )

    if ipaddr and macaddr:
        print('    Interface: %s, ip address: %s, mac address: %s.'\
            % ( port, ipaddr, macaddr ))
        
print('\nAnything else, please contact the company for professional service.')
