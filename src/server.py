import socket, threading

class ChatServer(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

        self.server = socket.socket()
        #self.host = socket.gethostbyname(socket.gethostname())

    def start_server(self, port):
        self.server.bind((socket.gethostname(), port))
        self.server.listen()
        self.server.accept()
    
    def send_message(self, message, username):
        self.server.sendall("{}: {}".format(username, message))
    
    def recv_message(self):
        while True:
            msg = self.recv()
            print(msg.decode("ascii"))