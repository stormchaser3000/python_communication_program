import socket

class ChatClient():
    def __init__(self, username, address):
        self.client = socket.socket()
        self.client.connect((address, 30000))
        connected_message = "{} connected\n".format(username)
        self.client.sendall(connected_message.encode("UTF-8"))

    def send_message(self, username, message):
        msg = "{}: {}\n".format(username, message)
        self.client.send(msg.encode('UTF-8'))

    def recieve_message(self, message_box):
        while True:
            msg = self.client.recv(1024)
            message_box.insert(END, msg)
