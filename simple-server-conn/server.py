#!/usr/bin/env python3

import socket

host = ''
port = 3500

if __name__ == '__main__':
    s = socket.socket()

    s.bind((host, port))

    s.listen(5)

    print(f'server is listening on port {port}')

    try:
        while True:
            conn, addr = s.accept()
            print(f"connected with {addr}")
            msg = f"you are successfully connected with server 127.0.0.1:{port}"
            conn.send(msg.encode('utf-8'))
            conn.close()
    finally:
        print('socket closing...')
        s.close()