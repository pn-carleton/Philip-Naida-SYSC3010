# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time
import random

host = sys.argv[1]
textport = sys.argv[2]
numMessage = sys.argv[3]

if numMessage < 0:
    print("num of messages to be sent must be positive")
    sys.exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

while 1:
    for i in range(0, int(numMessage)):
	number = str(random.randint(1, 100))
        s.sendto(number.encode('utf-8'), server_address)

s.shutdown(1)

