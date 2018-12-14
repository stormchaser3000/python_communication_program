import socket, _thread, selectors
from tkinter import *
# multithreading was not discussed in my programming class (this is here to indicate
# where a concept that was not taught in the class was used)
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", 30000))
    server.setblocking(True)
    server.listen()
    return server

def connection(connect, textbox):
    while True:
        msg = connect.recv(1024).decode("UTF-8")
        textbox.insert(END, msg)

def accept_connection(textbox, server):
    while True:
        connect, ip_addr = server.accept()
        _thread.start_new_thread(connection, (connect, textbox))

def send_message(server, message, username):
    server.sendall("{}: {}".format(username, message))
