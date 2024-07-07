#!/usr/bin/env python3

import sys
import socket
from datetime import datetime as dt

# define target
if len(sys.argv) == 2:
  target = socket.gethostbyname(sys.argv[1])
else:
  print("Invalid amount of arguments.")
  print("Syntax: python3 scanner.py <ip>")
  sys.exit()
  
# add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(dt.now()))
print("-" * 50)

try:
  for port in range(50, 85):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    print(f"Checking port {port}")
    if result == 0:
      print("Port {} is open".format(port))
    s.close()

except KeyboardInterrupt:
  print("\nExiting program.")
  sys.exit()

except socket.gaierror:
  print("hostname could not be resolved.")
  sys.exit()

except socket.error:
  print("Couldn't connect to server")
  sys.exit()