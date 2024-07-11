#!/usr/bin/env python3

import socket
import threading

host = '127.0.0.1'
port = 3500
alias = input('enter your alias: ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def receive():
  while True:
    try:
      msg = s.recv(1024).decode('utf-8')
      if msg == 'alias?':
        s.send(alias.encode('utf-8'))
      else:
        print(msg)
    except socket.error as err:
      print(f"an error occured: {err}")
      s.close()
      break

def send():
  while True:
    try:
      msg = input("")
      msg_full = f"{alias}: {msg}"
      s.send(msg_full.encode('utf-8'))
    except socket.error as err:
      print(f"an error occured: {err}")
      s.close()
      break

send_thread = threading.Thread(target=send)
send_thread.start()

recv_thread = threading.Thread(target=receive)
recv_thread.start()