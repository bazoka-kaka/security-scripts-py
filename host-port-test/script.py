#!/usr/bin/env python3

import socket

if __name__ == "__main__":
    domain = input("Enter domain to connect: ")
    port = int(input("Enter port to connect: "))

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostbyname(domain)
        s.settimeout(3)
        s.connect((host, port))
        print(f"successfully connected to {domain} on port {port}")
    except socket.gaierror:
        print("Failed resolving host")
    except socket.error as err:
        print(f"Failed to connect with error {err}")
    finally:
        s.close()