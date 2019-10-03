# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time
import random
import json


host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

age = 30

for i in range(0, 10):
    x = {"name": "John", "age": age, "city": "New York"}
    dump = json.dumps(x)
    s.sendto(dump.encode('utf-8'), server_address)
    age += 1

