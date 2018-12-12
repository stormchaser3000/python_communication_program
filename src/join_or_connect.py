from tkinter import ()

class JoinOrConnectWindow():
    def __init__(self):
        self.window = Tk()
    
    def create_frame(self):
        self.frame = Frame(self.window)
        self.frame.pack()
    
    def add_button(side=None, text=None, )