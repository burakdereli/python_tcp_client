import tcpClient
import socket
import time

host = socket.gethostname() #127.0.0.1
port = 10111
tcp1 = tcpClient.client(host,port)
print(tcp1)

while True:
    print(tcp1.connected())
    print(tcp1.receive())
    time.sleep(3)