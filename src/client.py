import socket

class ChatClient():
    def __init__(self):
        self.client = socket.socket()
    
    def connect(self, address, username):
        self.client.connect(address)
        self.client.sendall("{} connected".format(username))
    
    def send_message(self, username, message):
        self.client.sendall("{}: {}".format(username, message))
    
    def recv_message(self):
        while True:
            msg = self.recv()
            print(msg.decode("ascii"))