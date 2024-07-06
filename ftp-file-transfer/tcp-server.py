import socket

if __name__ == "__main__":
  host = "127.0.0.1"
  port = 8080
  totalClients = int(input("Enter clients total: "))
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind((host, port))
  sock.listen(totalClients)
  conns = []
  print("Initiating clients")

  # loop
  for i in range(totalClients):
    conn = sock.accept()
    conns.append(conn)
    print("connected with client", i + 1)
    
  fileno = 0
  idx = 0
  for conn in conns:
    idx += 1
    data = conn[0].recv(1024).decode()
    if not data:
      continue
    filename = 'output' + str(fileno) + '.txt'
    fileno += 1
    fo = open(filename, 'w')
    while data:
      if not data:
        break
      else:
        fo.write(data)
        data = conn[0].recv(1024).decode()
    print("\nReceiving file from client" + str(idx))
    print("\nReceived successfully! New filename is: " + filename)
    fo.close()

  # closing conns
  for conn in conns:
    conn[0].close()