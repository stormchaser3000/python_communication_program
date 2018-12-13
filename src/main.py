import _thread
import client, server

#window = chat_window.ChatWindow()

while True:
    try:
        print("Welcome to CypherChat")
        print("Would you like to join or connect to a server? (j or c)")
        option = input()

        if option == "j":
            c = client.ChatClient()

            print("Please enter the username that you would like to use\n:", end="")
            username = input()

            print("Please enter the ip address you would like to connect to\n:", end="")
            address = input()
            c.connect(address, username)
        elif:
            raise ValueError
    except:
        print("please enter c or j")
        continue



