#!/usr/bin/env python3

import sys
import socket
import threading
from datetime import datetime as dt

# define target
if len(sys.argv) == 2:
  target = socket.gethostbyname(sys.argv[1])
else:
  print("Invalid amount of arguments.")
  print("Syntax: python3 scanner.py <ip>")
  sys.exit()

# pretty banner
def print_banner():
  print("-" * 50)
  print("Scanning target: " + target)
  print("Time started: " + str(dt.now()))
  print("-" * 50)

def check_port(port):
  try:
    # socket.setdefaulttimeout(1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    # print(f"Checking port {port}")
    if result == 0:
      print("Port {} is open".format(port))
    s.close()
  except socket.gaierror:
    print("hostname could not be resolved.")
    sys.exit()
  except socket.error:
    print("Couldn't connect to server")
    sys.exit()

def scan_ports():
  try:
    for port in range(0, 65353):
      thread = threading.Thread(target=check_port, args=(port,))
      thread.start()

  except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

if __name__ == "__main__":
  scan_ports()