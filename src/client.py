import socket

class ChatClient():
    def __init__(self):
        self.client = socket.socket()
    
    def connect(self, address, username):
        self.client.connect((address, 30000))
        self.client.sendall("{} connected".format(username))
    
    def send_message(self, username, message):
        msg = "{}: {}".format(username, message)
        self.client.sendall(msg.encode('UTF-8'))
    
    def recv_message(self):
        while True:
            msg = self.recv()
            print(msg.decode("ascii"))