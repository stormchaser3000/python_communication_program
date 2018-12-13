import threading, _thread
import client, server, windows
from tkinter import *

jc = windows.JoinOrCreate()

# call the mainloop for the join or create window
jc.window.mainloop()

# start the chat window
cw = windows.ChatWindow(jc.username, jc.ip_addr)

# call the mainloop for the ChatWindow
cw.window.mainloop()

#while True:
#    print("Welcome to CypherChat")
#    print("Would you like to join or create a server? (j or c)")
#    option = input()

#    if option == "j":
#        print("Please enter the username that you would like to use\n:", end="")
#        username = input()

#        print("Please enter the ip address you would like to connect to\n:", end="")
#        address = input()

#        c = client.ChatClient()
#        c.connect(address, username)

#        while True:
#            message = input()
#            c.send_message(message, username)


#    elif option == "c":
#        s = server.ChatServer(threadID=1, name="Server")
#        s.start()

#        username = input("Please enter a username:")
#        while True:
#            message = input()
#            s.send_message(message, username)
#    else:
#        print("Please enter c or j")



