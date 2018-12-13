import socket, threading

class ChatServer(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

        self.server = socket.socket()

    def run(self):
        self.server.bind(('', 30000))
        self.server.listen(5)
        while True:
            connection, addr = self.server.accept()
            print(connection.recv(1024).decode('UTF-8'))
    
    def send_message(self, message, username):
        self.server.sendall("{}: {}".format(username, message))