#!/usr/bin/env python3
import socket

s = socket.socket()
s.bind(('', 3500))
s.listen(5)
print("server is listening on port 3500")

while True:
    c, addr = s.accept()
    print(f"connected to {addr}")
    msg = "successfully connected to server on port 3500"
    c.send(msg.encode('utf-8'))
    c.close()