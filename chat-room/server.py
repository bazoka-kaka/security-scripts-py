import threading
import socket

host = '127.0.0.1'
port = 3500

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

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
            idx = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[idx]
            broadcast(f"{alias} has left the chat room!".encode('utf-8'))
            aliases.remove(alias)
            break

# main function to receive clients conns
def receive():
    while True:
        print("Server is listening on port 3500")
        client, addr = server.accept()
        print(f"connection is established with {str(addr)}")
        client.send("alias?".encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f"Alias of this client is {alias}".encode('utf-8'))
        broadcast(f"{alias} has connected to the chat room".encode('utf-8'))
        client.send("You are now connected!".encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == '__main__':
    receive()