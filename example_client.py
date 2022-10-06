import tcpClient
import socket
import time

host = socket.gethostname() #127.0.0.1
port = 10111
tcp1 = tcpClient.client(host,port)
print(tcp1)

while True:
    print(tcp1.connected())
    if tcp1.connected():
        rcv = tcp1.receive()
        print(rcv)
    time.sleep(3)