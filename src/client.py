import socket, threading

class ChatClient(threading.Thread):
    def __init__(self, username, address):
        threading.Thread.__init__(self)
        self.client = socket.socket()
        self.username = username
        self.address = address
    
    def run(self):
        self.client.connect((self.address, 30000))
        connected_message = "{} connected".format(self.username)
        self.client.sendall(connected_message.encode("UTF-8"))
    
    def send_message(self, username, message):
        msg = "{}: {}".format(username, message)
        self.client.sendall(msg.encode('UTF-8'))
    
    def recv_message(self):
        while True:
            msg = self.recv()
            print(msg.decode("ascii"))