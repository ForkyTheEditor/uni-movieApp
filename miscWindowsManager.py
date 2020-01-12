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



    def openOrderMovieWindow(self):

        pass

