from Tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E
import random

def is_valid_ipv4(ip):
    parts = ip.split('.')

    return (    len(parts) == 4
                and all(part.isdigit() for part in parts)
                and all(0 <= int(part) <= 255 for part in parts)
           )

class Master:
    def __init__(self, master):
        self.master = master
        master.title("HTTP FLOOD")


        self.IP = None


        self.message = "Type IP to be attacked:"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.atack_button = Button(master, text="Start Atack", command=self.validate_IP)
        self.stop_button = Button(master, text="Stop Atack", command=self.reset, state=DISABLED)

        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.atack_button.grid(row=2, column=0)
        self.stop_button.grid(row=2, column=1)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.IP = None
            return True
        else:
            IP = new_text
            self.IP=IP
            return True

    def validate_IP(self):

        if (is_valid_ipv4(str(self.IP))):
            self.message = "Valid IP, Contacting Slaves!"
            self.atack_button.configure(state=DISABLED)
            self.stop_button.configure(state=NORMAL)
        else:
            self.message = "Invalid IP, Try Again"

        if self.IP is None:
            self.message = "Type IP to be attacked:"

        self.label_text.set(self.message)

    def reset(self):
        self.entry.delete(0, END)

        self.IP = None

        self.message = "Type IP to be attacked:"
        self.label_text.set(self.message)

        self.atack_button.configure(state=NORMAL)
        self.stop_button.configure(state=DISABLED)

root = Tk()
my_gui = GuessingGame(root)
root.mainloop()