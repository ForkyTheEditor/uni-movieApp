import tkinter as tk
from userManager import User

class UserWindow():

    def __init__(self, master, userList):

        master.title("RipOff™ Movie Store: Users")
        master.geometry("450x450")

        self.userList = userList

        self.frame = tk.Frame(master, bd = 20)
        self.frame.pack(side = tk.TOP, fill = tk.BOTH)

        self.scrollY = tk.Scrollbar(self.frame, orient=tk.VERTICAL) 
        self.scrollX = tk.Scrollbar(self.frame, orient = tk.HORIZONTAL)
        self.list = tk.Listbox(self.frame, yscrollcommand=self.scrollY.set, xscrollcommand = self.scrollX.set)
        
        self.scrollY.config(command = self.list.yview)
        self.scrollX.config(command = self.list.xview)
        
        self.list.pack(side = tk.TOP, fill = tk.X)
        self.scrollY.pack(side = tk.RIGHT, fill = tk.Y)
        self.scrollX.pack(side = tk.BOTTOM, fill = tk.X)

        self.buttonFrame = tk.Frame(master, bd = 20)
        self.buttonFrame.pack(side = tk.TOP)

        self.addUserButton = tk.Button(self.buttonFrame, text = "Add User", command = self.printshit)
        self.addUserButton.pack(side = tk.TOP, fill = tk.X)

        self.updateUserButton = tk.Button(self.buttonFrame, text = "Update User's last name", command = self.printshit)
        self.updateUserButton.pack(side = tk.TOP, fill = tk.X)

    def printshit(self):

        print("shit")