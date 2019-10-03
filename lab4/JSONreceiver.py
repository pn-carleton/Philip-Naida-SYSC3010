# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time
import json

textport = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

for i in range(0,10):

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

    buf, address = s.recvfrom(port)
    if not len(buf):
        break
    x = json.loads(buf)
    print ("Received %s bytes from %s: " % (len(buf), address))
    print(x)

