#!/usr/bin/env python3

import socket

s = socket.socket()
host = '127.0.0.1'
port = 3500
s.connect((host, port))

data = s.recv(1024)

print(data.decode('utf-8'))

s.close()