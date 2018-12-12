from tkinter import *

class ChatWindow():
    window = Tk()

    window.geometry("480x480+{:.0f}+{:.0f}".format((int(window.winfo_screenwidth()) / 2),
    (int(window.winfo_screenheight()) / 2)))

    window.mainloop()