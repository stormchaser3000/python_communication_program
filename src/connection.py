import socket

class Server():
    def __init__(self, port):
        self.server = socket.socket()

        self.host = socket.gethostbyname(socket.gethostname())
        self.server.bind(self.host, self.port)

    def start_server(self):
        self.server.listen()

        while True:
            self.server.accept()