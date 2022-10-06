import socket

class client:
    def __init__(self, ip, port):
        try:
            self.ip = ip
            self.port = port
            self.tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcpClient.settimeout(0.001)
            self.tcpClient.connect((self.ip, self.port))
            self.tcpClient.sendall(b'Hello, world')
            print("TCP Connection Done")
            self.isOK = True
        except:
            print("TCP Connection Error")
    def connected(self):
        try:
            if not self.isOK:
                self.tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.tcpClient.settimeout(0.001)
                self.tcpClient.connect((self.ip, self.port))
                self.isOK = True
            get = self.tcpClient.getpeername()
            return True
        except:
            self.isOK = False
            return False
    def receive(self):
        if self.isOK:
            try:
                data = self.tcpClient.recv(1024).decode()
                if data:
                    return data
                else: #tcp bağlantısı koptu
                    self.isOK = False
                    return None
            except:
                return ""
        else:
            return None
    def sendData(self,sendData):
        if self.isOK:
            try:
                if len(sendData) > 0:
                    self.tcpClient.sendall(bytes(sendData, 'utf-8'))
            except:
                return ""
        else:
            return False
