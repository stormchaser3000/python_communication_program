import threading, _thread
import client, server

#window = chat_window.ChatWindow()

while True:
    print("Welcome to CypherChat")
    print("Would you like to join or create a server? (j or c)")
    option = input()

    if option == "j":
        c = client.ChatClient()

        print("Please enter the username that you would like to use\n:", end="")
        username = input()

        print("Please enter the ip address you would like to connect to\n:", end="")
        address = input()
        ip_addr = ()
        for i in address:
            ip_addr.append(i)
        c.connect(address, username)

        while True:
            message = input()
            c.send_message(message, username)


    elif option == "c":
        s = server.ChatServer(threadID=1, name="Server")

        username = input("Please enter a username:")

        _thread.start_new_thread(s.recv_message)
        while True:
            message = input()
            s.send_message(message, username)
    else:
        print("Please enter c or j")



