import tkinter as tk
from tkinter import messagebox
from userManager import User
from moviesManager import Movie

class MiscWindow():
    """ Class for creating the Misc Functions window """


    def __init__(self, master, movieList, userList):
        
        master.title("RipOff™ Movie Store: Common")
        master.geometry("450x450")

        self.movieList = movieList
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

        self.orderMovieButton = tk.Button(self.buttonFrame, text = "Order Movie", command = self.openOrderMovieWindow)
        self.orderMovieButton.pack(side = tk.TOP, fill = tk.X)

        self.searchMovieButton = tk.Button(self.buttonFrame, text = "Search Movie by rating", command = self.openOrderMovieWindow)
        self.searchMovieButton.pack(side = tk.TOP, fill = tk.X)

        self.filterMoviesButton = tk.Button(self.buttonFrame, text = "Filter Movies by actor", command = self.openOrderMovieWindow)
        self.filterMoviesButton.pack(side = tk.TOP, fill = tk.X)


    def updateUserList(self):

        self.list.delete(0, tk.END)

        for user in self.userList:

            self.list.insert(tk.END, str(user))

    def openOrderMovieWindow(self):

        top = tk.Toplevel()
        orderWindow = OrderMovieWindow(top, self.userList, self.movieList, self)


class OrderMovieWindow():

    def __init__(self, master, userList, movieList, parentWindow):
        
        master.title("RipOff™ Movie Store: Order movie")
        self.master = master

        self.userList = userList
        self.movieList = movieList
        self.parentWindow = parentWindow

        self.frame = tk.Frame(master, bd = 20)
        self.frame.pack(side = tk.TOP)
        
        self.ordersFrame = tk.Frame(master)
        self.ordersFrame.pack(side = tk.BOTTOM)
        
        self.chooseUserLabel = tk.Label(self.frame, text = "Choose user index")
        self.chooseUserLabel.pack(side = tk.LEFT)
        self.chooseUserEntry = tk.Entry(self.frame)
        self.chooseUserEntry.pack(side = tk.LEFT)

        self.ordersLabel = tk.Label(self.ordersFrame, text = "Orders Index (separate by NewLine):")
        self.ordersLabel.pack(side = tk.LEFT)
        self.ordersText = tk.Text(self.ordersFrame)
        self.ordersText.pack(side = tk.LEFT)

        self.submitButton = tk.Button(self.ordersFrame, text = "Submit", bg = "grey", command = self.SubmitOrder)
        self.submitButton.pack(side = tk.RIGHT, fill = tk.BOTH)


    def SubmitOrder(self):

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
            orderData = self.ordersText.get("1.0",'end-1c')
            newOrdersRawData = orderData.splitlines()
            
        except ValueError:
            messagebox.showerror("Value error", "Order list not properly defined!")

        newOrders = []
        newOrderNumbers = []


        #Transform list into valid list of integers
        for item in newOrdersRawData:

            try:
                item = int(item)
            except ValueError:
                continue
            
                
            
            if item >= 0 and item < len(self.movieList):

                newOrderNumbers.append(item)
        
        #Add the corresponding orders 
        for number in newOrderNumbers:

            newOrders.append(str(self.movieList[number]))

        self.userList[userId].orders.extend(newOrders)
        self.parentWindow.updateUserList()
        self.master.destroy()




