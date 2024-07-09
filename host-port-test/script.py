#!/usr/bin/env python3

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket successfully created!")
except socket.error as err:
    print(f"socket creation failed with error: {err}")
    sys.exit()

domain = input("Enter domain to connect: ")
port = int(input("Enter port to connect: "))

try:
    host = socket.gethostbyname(domain)
    print("socket successfully connected to the host!")
except socket.gaierror:
    print("error resolving host")
    sys.exit()

s.connect((host, port))
print(f"successfully connected to {domain} on port {port}")