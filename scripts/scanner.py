#! /usr/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    # hostname from the args to ip address
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Invalid amount of argument')
    print('Syntax is: scanner.py <ip address>')
    sys.exit

# add a banner in terminal for prettier look

print('*' * 50)
print('Scanning target with address ' + target)
print('Time started '+str(datetime.now()))
print('*' * 50)

try:
    for port in range(1, 1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        print('Checking port {}' .format(port))
        if result == 0:
            print('port {} is open '.format(port))
        s.close

except KeyboardInterrupt:
    print('Quitting program')
    sys.exit
except socket.gaierror:
    print('hostname could not be resolved')
except socket.error:
    print('could not connect to server')



