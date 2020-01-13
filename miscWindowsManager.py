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

        self.orderMovieButton = tk.Button(self.buttonFrame, text = "Order Movie", bg = "grey",command = self.openOrderMovieWindow)
        self.orderMovieButton.pack(side = tk.TOP, fill = tk.X)

        self.searchMovieButton = tk.Button(self.buttonFrame, text = "Search Movie by rating",bg = "grey", command = self.openSearchRatingWindow)
        self.searchMovieButton.pack(side = tk.TOP, fill = tk.X)

        self.filterMoviesButton = tk.Button(self.buttonFrame, text = "Filter Movies by actor",bg = "grey", command = self.openSearchActorWindow)
        self.filterMoviesButton.pack(side = tk.TOP, fill = tk.X)


    def updateUserList(self):

        self.list.delete(0, tk.END)

        for user in self.userList:

            self.list.insert(tk.END, str(user))

    def openOrderMovieWindow(self):

        top = tk.Toplevel()
        orderWindow = OrderMovieWindow(top, self.userList, self.movieList, self)

    def openSearchRatingWindow(self):

        top = tk.Toplevel()
        searchWindow = SearchMoviesRatingWindow(top, self.movieList)

    def openSearchActorWindow(self):

        top = tk.Toplevel()
        searchWindow = SearchMoviesActorWindow(top, self.movieList)


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
        finalPrice = 0

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
            finalPrice += self.movieList[number].price

        self.userList[userId].orders.extend(newOrders)
        self.parentWindow.updateUserList()
        messagebox.showerror("Total Price", "Total price of the order: " + str(finalPrice))
        self.master.destroy()

class SearchMoviesRatingWindow():

    def __init__(self, master, movieList):
        
        master.title("RipOff™ Movie Store: Search Movies")

        self.master = master

        self.movieList = movieList

        self.frame = tk.Frame(master, bd = 20)
        self.frame.pack(side = tk.TOP)

        self.chooseRatingLabel = tk.Label(self.frame, text = "Rating higher than:")
        self.chooseRatingLabel.pack(side = tk.LEFT)
        self.chooseRatingEntry = tk.Entry(self.frame)
        self.chooseRatingEntry.pack(side = tk.LEFT)

        self.submitButton = tk.Button(self.frame, text = "Submit", bg = "grey", command = self.SubmitRating)
        self.submitButton.pack(side = tk.RIGHT, fill = tk.BOTH)


    def SubmitRating(self):

        try:

            rating = float(self.chooseRatingEntry.get())
        except ValueError:

            messagebox.showerror("Value Error", "Rating is not a float!")
            self.master.destroy()
            return

        moviesToShow = []

        for movie in self.movieList:

            if movie.rating >= rating:

                moviesToShow.append(movie)

        listTop = tk.Toplevel()
        listWindow = ShowList(listTop, moviesToShow, self.master)
         

        listTop.mainloop()

class SearchMoviesActorWindow():

    def __init__(self, master, movieList):
        
        master.title("RipOff™ Movie Store: Search Movies by actor")

        self.master = master

        self.movieList = movieList

        self.frame = tk.Frame(master, bd = 20)
        self.frame.pack(side = tk.TOP)

        self.chooseActorLabel = tk.Label(self.frame, text = "Actor:")
        self.chooseActorLabel.pack(side = tk.LEFT)
        self.chooseActorEntry = tk.Entry(self.frame)
        self.chooseActorEntry.pack(side = tk.LEFT)

        self.submitButton = tk.Button(self.frame, text = "Submit", bg = "grey", command = self.SubmitActor)
        self.submitButton.pack(side = tk.RIGHT, fill = tk.BOTH)

    def SubmitActor(self):

        actorToSearch = self.chooseActorEntry.get()

        moviesToShow = []

        for movie in self.movieList:

            for actor in movie.actors:

                if actor == actorToSearch:

                    moviesToShow.append(movie)
                    break
        
        listTop = tk.Toplevel()
        listWindow = ShowList(listTop, moviesToShow, self.master)
         

        listTop.mainloop()


class ShowList():

    def __init__(self, master, listToShow, entryWindowMaster):


        master.title("RipOff™ Movie Store: Search Movies")

        self.master = master
        self.entryWindowMaster = entryWindowMaster

        self.frame = tk.Frame(master, bd = 20)
        self.frame.pack(side = tk.TOP)

        self.scrollY = tk.Scrollbar(self.frame, orient=tk.VERTICAL) 
        self.scrollX = tk.Scrollbar(self.frame, orient = tk.HORIZONTAL)
        self.list = tk.Listbox(self.frame, yscrollcommand=self.scrollY.set, xscrollcommand = self.scrollX.set)
        
        self.scrollY.config(command = self.list.yview)
        self.scrollX.config(command = self.list.xview)
        
        self.list.pack(side = tk.TOP, fill = tk.X)
        self.scrollY.pack(side = tk.RIGHT, fill = tk.Y)
        self.scrollX.pack(side = tk.BOTTOM, fill = tk.X)

        for item in listToShow:

            self.list.insert(tk.END, str(item))

        self.submitButton = tk.Button(self.frame, text = "Okay", bg = "grey", command = self.ExitWindow)
        self.submitButton.pack(side = tk.RIGHT, fill = tk.BOTH)

    def ExitWindow(self):

        self.entryWindowMaster.destroy()
        self.master.destroy()