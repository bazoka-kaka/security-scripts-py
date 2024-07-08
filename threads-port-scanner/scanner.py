from socket import *
from time import time

startTime = time()

if __name__ == "__main__":
  target = input("Enter host ip: ")
  host = gethostbyname(target)
  print(f"Scanning on host {host}")
  
  for port in range(500):
    s = socket(AF_INET, SOCK_STREAM)
    
    conn = s.connect_ex((host, port))
    
    if conn == 0:
      print(f"Port {str(port)} is OPEN")
    s.close()
  
print(f"Time taken: {str(time.time() - startTime)}")