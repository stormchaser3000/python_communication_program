import socket, _thread, selectors
from tkinter import *

connected_list = []

def send_to_others(msg, conn):
    for connenected in connected_list:
        if connected != conn:
            try:
                connected.send(msg)
            except:
                clients.close()
                connected_list.remove(connected)

def connection_handling(serv, addr):
    while True:
        info = serv.recv(2048).decode("utf-8")

        send_to_others(info, serv)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 30000))
    print("Bound socket to 0.0.0.0")
    server.setblocking(True)
    server.listen()
    print("server is listening")
    while True:
        connect, ip_addr = server.accept()
        print("Connected to:", ip_addr)
        connected_list.append(connect)
        _thread.start_new_thread(connection_handling, (connect, ip_addr))
