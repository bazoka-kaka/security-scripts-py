#!/usr/bin/env python3

import socket
import threading

host = '127.0.0.1'
port = 3500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)

clients = []
aliases = []

def broadcast(msg):
  for client in clients:
    client.send(msg)

def handle_client(client):
  while True:
    try:
      msg = client.recv(1024)
      broadcast(msg)
    except:
      idx = clients.index(idx)
      clients.remove(client)
      client.close()
      alias = aliases[idx]
      msg = f"{alias} left the chatroom"
      print(msg)
      broadcast(msg.encode('utf-8'))
      client.send("you left the chatroom!".encode("utf-8"))
      aliases.remove(alias)
      break

def receive():
  while True:
    print(f"server is listening on port {port}")
    conn, addr = s.accept()
    print(f"connection established with {str(addr)}")
    conn.send("alias?".encode('utf-8'))
    alias = conn.recv(1024).decode('utf-8')
    print(f"alias of the client: {alias}")
    broadcast(f"{alias} joined the chatroom".encode('utf-8'))
    conn.send("successfully connected to the chatroom".encode('utf-8'))
    clients.append(conn)
    aliases.append(alias)
    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()
    
if __name__ == "__main__":
  receive()