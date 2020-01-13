import tkinter as tk
from userManager import User
from tkinter import messagebox

class UserWindow():

    def __init__(self, master, userList, commonWindowObject):

        master.title("RipOff™ Movie Store: Users")
        master.geometry("450x450")

        self.commonWindowObject = commonWindowObject

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

        self.addUserButton = tk.Button(self.buttonFrame, text = "Add User", bg = "grey",command = self.openAddUserWindow)
        self.addUserButton.pack(side = tk.TOP, fill = tk.X)

        self.updateUserButton = tk.Button(self.buttonFrame, text = "Update User",bg = "grey", command = self.openUpdateUserWindow)
        self.updateUserButton.pack(side = tk.TOP, fill = tk.X)

        self.removeUserButton = tk.Button(self.buttonFrame, text = "Remove User",bg = "grey", command = self.openRemoveUserWindow)
        self.removeUserButton.pack(side = tk.TOP, fill = tk.X)

        

    def openAddUserWindow(self):


        top = tk.Toplevel()
        addWindow = AddUserWindow(top, self.userList, self.list, self.commonWindowObject)

    def openUpdateUserWindow(self):

        top = tk.Toplevel()
        updateWindow = UpdateUserWindow(top, self.userList, self.list, self.commonWindowObject)
       
    def openRemoveUserWindow(self):

        top = tk.Toplevel()
        removeWindow = RemoveUserWindow(top, self.userList, self.list, self.commonWindowObject)


class AddUserWindow():

    def __init__(self, master, userList, listbox, commonWindowObject):

        master.title("RipOff™ Movie Store: Add User")
        self.master = master

        self.commonWindowObject = commonWindowObject

        self.userList = userList
        self.listbox = listbox

        self.frame = tk.Frame(master, bd = 20)
        self.frame.pack(side = tk.TOP)

        self.ordersFrame = tk.Frame(master)
        self.ordersFrame.pack(side = tk.BOTTOM)

        self.firstNameLabel = tk.Label(self.frame, text = "First name: ")
        self.firstNameLabel.pack(side = tk.LEFT)
        self.firstNameEntry = tk.Entry(self.frame)
        self.firstNameEntry.pack(side = tk.LEFT)

        self.lastNameLabel = tk.Label(self.frame, text = "Last name: ")
        self.lastNameLabel.pack(side = tk.LEFT)
        self.lastNameEntry = tk.Entry(self.frame)
        self.lastNameEntry.pack(side = tk.LEFT)

        self.ordersLabel = tk.Label(self.ordersFrame, text = "Orders (separate by NewLine):")
        self.ordersLabel.pack(side = tk.LEFT)
        self.ordersText = tk.Text(self.ordersFrame)
        self.ordersText.pack(side = tk.LEFT)
        
        self.submitButton = tk.Button(self.ordersFrame, text = "Submit", bg = "grey", command = self.SubmitUserDetails)
        self.submitButton.pack(side = tk.RIGHT, fill = tk.BOTH)

    def SubmitUserDetails(self):


        try:
            newFName = self.firstNameEntry.get()
        except ValueError:
            messagebox.showerror("Value error", "First name not a string!")

        try:
            newLName = self.lastNameEntry.get()
        except ValueError:
            messagebox.showerror("Value error", "Last name not a string!")

        try:
            orderData = self.ordersText.get("1.0",'end-1c')
            newOrders = orderData.splitlines()
            
        except ValueError:
            messagebox.showerror("Value error", "Order list not properly defined!")

        newUser = User(newFName, newLName, newOrders)

        self.userList.append(newUser)
        self.listbox.insert(tk.END, str(newUser))
        self.commonWindowObject.updateUserList()
        self.master.destroy()


class UpdateUserWindow():

    def __init__(self, master, userList, listbox, commonWindowObject):

        master.title("RipOff™ Movie Store: Update User")
        self.master = master

        self.commonWindowObject = commonWindowObject

        self.userList = userList
        self.listbox = listbox

        self.frame = tk.Frame(master, bd = 20)
        self.frame.pack(side = tk.TOP)

        self.ordersFrame = tk.Frame(master)
        self.ordersFrame.pack(side = tk.BOTTOM)

        self.helpLabel = tk.Label(self.frame, text = "LEAVE BLANK FOR UNCHANGED")
        self.helpLabel.pack(side = tk.TOP)

        self.chooseUserLabel = tk.Label(self.frame, text = "Choose user index")
        self.chooseUserLabel.pack(side = tk.LEFT)
        self.chooseUserEntry = tk.Entry(self.frame)
        self.chooseUserEntry.pack(side = tk.LEFT)

        self.firstNameLabel = tk.Label(self.frame, text = "First name: ")
        self.firstNameLabel.pack(side = tk.LEFT)
        self.firstNameEntry = tk.Entry(self.frame)
        self.firstNameEntry.pack(side = tk.LEFT)

        self.lastNameLabel = tk.Label(self.frame, text = "Last name: ")
        self.lastNameLabel.pack(side = tk.LEFT)
        self.lastNameEntry = tk.Entry(self.frame)
        self.lastNameEntry.pack(side = tk.LEFT)

        self.ordersLabel = tk.Label(self.ordersFrame, text = "Orders (separate by NewLine):")
        self.ordersLabel.pack(side = tk.LEFT)
        self.ordersText = tk.Text(self.ordersFrame)
        self.ordersText.pack(side = tk.LEFT)
        
        self.submitButton = tk.Button(self.ordersFrame, text = "Submit", bg = "grey", command = self.SubmitUserDetails)
        self.submitButton.pack(side = tk.RIGHT, fill = tk.BOTH)

    def SubmitUserDetails(self):

        try:
            userId = int(self.chooseUserEntry.get())
            if userId >= len(self.userList):
                userId = len(self.userList) - 1
            elif userId < 0:
                userId = 0

        except ValueError:
            messagebox.showerror("Value error", "ID not an integer!")
            self.master.destroy()
            return


        try:
            newFName = self.firstNameEntry.get()
            if newFName in ['', None]:
                newFName = self.userList[userId].firstName

        except ValueError:
            messagebox.showerror("Value error", "First name not a string!")
            newFName = self.userList[userId].firstName


        try:
            newLName = self.lastNameEntry.get()
            if newLName in ['', None]:
                newLName = self.userList[userId].lastName

        except ValueError:
            messagebox.showerror("Value error", "Last name not a string!")
            newLName = self.userList[userId].lastName


        try:
            orderData = self.ordersText.get("1.0",'end-1c')
            newOrders = orderData.splitlines()
            if newOrders in ['', None]:
                newOrders = self.userList[userId].orders
            
        except ValueError:
            messagebox.showerror("Value error", "Order list not properly defined!")
            newOrders = self.userList[userId].orders

        newUser = User(newFName, newLName, newOrders)

        
        self.userList[userId] = newUser
        self.listbox.delete(userId)
        self.listbox.insert(userId, str(self.userList[userId]))
        self.commonWindowObject.updateUserList()

        self.master.destroy()

class RemoveUserWindow():

    def __init__(self, master, userList, listbox, commonWindowObject):

        self.listbox = listbox
        self.master = master
        self.userList = userList

        self.commonWindowObject = commonWindowObject

        self.frame = tk.Frame(master, bd = 20)
        self.frame.pack(side = tk.TOP)

        self.removeLabel = tk.Label(self.frame, text = "User Index:")
        self.removeLabel.pack(side = tk.LEFT)
        self.removeEntry = tk.Entry(self.frame)
        self.removeEntry.pack(side = tk.LEFT)
        
        self.submitButton = tk.Button(self.frame, text = "Submit", bg = "grey", command = self.SubmitUser)
        self.submitButton.pack(side = tk.RIGHT, fill = tk.BOTH)

    def SubmitUser(self):


        try:

            indexToRemove = int(self.removeEntry.get())
        except ValueError:
            messagebox.showerror("Value error", "Index is not an integer!")
            self.master.destroy()
            return

        if 0 <= indexToRemove and indexToRemove < len(self.userList):

            messagebox.showerror("Value error", "Index out of range!")
            self.master.destroy()
            return

        del self.userList[indexToRemove]
        self.listbox.delete(indexToRemove)
        self.commonWindowObject.updateUserList()

        self.master.destroy()


            
