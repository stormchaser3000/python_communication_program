from tkinter import *
import client, server, _thread

class JoinOrCreate():
    def __init__(self):
        # create a tkinter window
        self.window = Tk()

        # set the window geometry and title
        self.window.title("join or create")
        self.window.geometry("250x100+{:.0f}+{:.0f}".format((self.window.winfo_screenwidth() / 2), (self.window.winfo_screenheight() / 2)))
        self.window.resizable(width=True, height=True)

        # create a frame to organize widgets
        self.frame_top = Frame(self.window)
        self.frame_top.pack()

        # create a button that creates the join dialog
        self.join_button = Button(self.frame_top, text="Join", command=self.join_username_dialog)
        self.join_button.pack(side=TOP)

        # create another frame to help organize widgets
        self.frame_bottom = Frame(self.frame_top)
        self.frame_bottom.pack(side=BOTTOM)

        # display the word "or"
        self.label = Label(self.frame_bottom, text="or")
        self.label.pack(side=TOP)

        # create the "create" button that displays the create server dialog
        self.create_button = Button(self.frame_bottom, text="Create", command=self.username_dialog_create)
        self.create_button.pack(side=BOTTOM)

    def join_username_dialog(self):
        self.join = True
        self.window.title("Join")

        # destroy some widgets
        self.join_button.pack_forget()
        self.join_button.destroy()

        self.label.pack_forget()
        self.label.destroy()

        self.create_button.pack_forget()
        self.create_button.destroy()

        # join dialog (username entry)
        self.window.geometry("240x100")

        self.label = Label(self.frame_top, text="Please enter a username")
        self.label.pack(side=TOP)

        self.username_entry = Entry(self.frame_bottom, width=20)
        self.username_entry.pack(side=TOP)

        self.next_button = Button(self.frame_bottom, text="Next", command=self.next_dialog)
        self.next_button.pack(side=BOTTOM)

    def username_dialog_create(self):
        self.join = False
        self.window.title("Create")

        # destroy some widgets
        self.join_button.pack_forget()
        self.join_button.destroy()

        self.label.pack_forget()
        self.label.destroy()

        self.create_button.pack_forget()
        self.create_button.destroy()

        # join dialog (username entry)
        self.window.geometry("240x100")

        self.label = Label(self.frame_top, text="Please enter a username")
        self.label.pack(side=TOP)

        self.username_entry = Entry(self.frame_bottom, width=20)
        self.username_entry.pack(side=TOP)

        self.next_button = Button(self.frame_bottom, text="Next", command=self.next_dialog)
        self.next_button.pack(side=BOTTOM)

    def next_dialog(self):
        if self.join == False:
            # store the username for later use
            self.username = self.username_entry.get()
            # destroy the window if creating a server instead of joining one
            self.window.destroy()

            self.ip_addr = ""

        elif self.join == True:
            # store the username for later use
            self.username = self.username_entry.get()
            # destroy some widgets
            self.username_entry.pack_forget()
            self.username_entry.destroy()

            self.next_button.pack_forget()
            self.next_button.destroy()

            self.frame_bottom.pack_forget()
            self.frame_bottom.destroy()

            # enter ip address dialog
            self.label.configure(text="ip address")
            self.ip_entry = Entry(self.frame_top, width=20)
            self.ip_entry.pack(side=TOP)

            self.join_button = Button(self.frame_top, text="Connect to server", command=self.end_window)
            self.join_button.pack(side=BOTTOM)

    def end_window(self):
        # store the ip address before destroying the window
        self.ip_addr = self.ip_entry.get()

        # destroy the join or create dialog
        self.window.destroy()

class ChatWindow():
    def __init__(self, username, ip_addr, join):
        # store the username and ip address
        self.username = username
        self.address = ip_addr

        # create the chat window
        self.window = Tk()
        self.window.geometry("700x400+{:.0f}+{:.0f}".format((self.window.winfo_screenwidth() / 2), (self.window.winfo_screenheight() / 2)))
        self.window.resizable(width=False, height=False)

        self.frame_left = Frame(self.window, width=20)
        self.frame_left.pack(side=LEFT, fill=Y, expand=True)

        # create the user list
        self.user_list = Listbox(self.frame_left, width=20, selectmode=EXTENDED)
        self.user_list.pack(side=LEFT, fill=Y, expand=True)
        self.user_list.insert(0, self.username)

        # create the frame to put the message box and message entry into
        self.frame_right = Frame(self.window)
        self.frame_right.pack(side=RIGHT, fill=BOTH, expand=True)

        # create the top right frame and the bottom right frame
        self.frame_right_top = Frame(self.frame_right, pady=0)
        self.frame_right_top.pack(side=TOP, fill=BOTH, expand=True)

        self.frame_right_bottom = Frame(self.frame_right, height=1, pady=0)
        self.frame_right_bottom.pack(side=BOTTOM, fill=X, expand=True)

        # create a read-only message box and put it into the frame
        self.message_box = Text(self.frame_right_top)
        self.message_box.pack(side=TOP, fill=BOTH, expand=True, pady=0)
        self.message_box.config(state=DISABLED)

        # create the place to enter chat messages into
        self.message_entry = Entry(self.frame_right_bottom)
        self.message_entry.pack(side=BOTTOM, fill=X, expand=True, pady=0, ipady=1)

        self.send_button = Button(self.frame_right_bottom, text="Send", command=lambda: self.send_message(self.message_entry.get(), self.username))
        self.send_button.pack(side=RIGHT)

        # connect to server if join is True or start one if False
        if join == True:
            self.cli = client.ChatClient(self.username, self.address)
            _thread.start_new_thread(self.cli.recieve_message, (self.message_box, ))
        elif join == False:
            self.serv = server.start_server()
            _thread.start_new_thread(server.accept_connection,(self.message_box, self.serv))
    def send_message(self, message, username):
        if join == True:
            self.cli.send_message(username, message)
        else:
            server.send_message(self.serv, message, username)
