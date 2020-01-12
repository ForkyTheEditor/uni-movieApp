import tkinter as tk
from tkinter import messagebox
from moviesManager import Movie

class MovieWindow():
    """ Class for creating the Main Movie window """


    def __init__(self, master, movieList):
        
        master.title("RipOff™ Movie Store: Movies")
        master.geometry("450x450")

        self.movieList = movieList

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

        self.addMovieButton = tk.Button(self.buttonFrame, text = "Add Movie", command = self.openAddMovieWindow)
        self.addMovieButton.pack(side = tk.TOP, fill = tk.X)

        self.updateMovieButton = tk.Button(self.buttonFrame, text = "Update Movie", command = self.openUpdateMovieWindow)
        self.updateMovieButton.pack(side = tk.TOP, fill = tk.X)

    


    def openAddMovieWindow(self):
        """ Opens a new add movie window """

        #CREATE THE ADD MOVIE INTERFACE
        top = tk.Toplevel()
        addWindow = AddMovieWindow(top, self.movieList, self.list)

    def openUpdateMovieWindow(self):
        """ Opens a new update movie window """

        top = tk.Toplevel()
        updateWindow = UpdateMovieWindow(top, self.movieList, self.list)        
        

        

    

class AddMovieWindow():
    """ Class for creating the Add Movie window """

    def __init__(self, master, movieList, listbox):
        
        #-----<INTERFACE>-----------

        self.movieList = movieList
        self.listbox = listbox
        self.master = master

        self.frame = tk.Frame(master, bd = 20)
        self.frame.pack(side = tk.TOP)

        self.actorsFrame = tk.Frame(master)
        self.actorsFrame.pack(side = tk.BOTTOM)

        self.titleLabel = tk.Label(self.frame, text = "Title:")
        self.titleLabel.pack(side = tk.LEFT)
        self.titleEntry = tk.Entry(self.frame)
        self.titleEntry.pack(side = tk.LEFT)

        self.yearLabel = tk.Label(self.frame, text = "Year:")
        self.yearLabel.pack(side = tk.LEFT)
        self.yearEntry = tk.Entry(self.frame)
        self.yearEntry.pack(side = tk.LEFT)

        self.ratingLabel = tk.Label(self.frame, text = "Rating:")
        self.ratingLabel.pack(side = tk.LEFT)
        self.ratingEntry = tk.Entry(self.frame)
        self.ratingEntry.pack(side = tk.LEFT)

        self.actorsLabel = tk.Label(self.actorsFrame, text = "Actors (separate by NewLine):")
        self.actorsLabel.pack(side = tk.LEFT)
        self.actorsText = tk.Text(self.actorsFrame)
        self.actorsText.pack(side = tk.LEFT)

        self.priceLabel = tk.Label(self.frame, text = "Price:")
        self.priceLabel.pack(side = tk.LEFT)
        self.priceEntry = tk.Entry(self.frame)
        self.priceEntry.pack(side = tk.LEFT)
        
        self.submitButton = tk.Button(self.actorsFrame, text = "Submit", bg = "grey", command = self.SubmitMovieDetails)
        self.submitButton.pack(side = tk.RIGHT, fill = tk.BOTH)

        #-----</INTERFACE>-----------


    def SubmitMovieDetails(self):
    

        try:
            newTitle = self.titleEntry.get()
        except ValueError:
            messagebox.showerror("Value error", "Title not a string!")
            

        try:
            newRating = float(self.ratingEntry.get())
        except ValueError:
            messagebox.showerror("Value error", "Rating not a float! Taking default value...")
            newRating = 0

        try:
            newYear = int(self.yearEntry.get())
        except ValueError:
            messagebox.showerror("Value error", "Year not an integer! Taking default value...")
            newYear = 0

        try:
            actorData = self.actorsText.get("1.0",'end-1c')
            newActors = actorData.splitlines()
            
        except ValueError:
            messagebox.showerror("Value error", "Actor list not properly defined!")
           
        try: 
            newPrice = float(self.priceEntry.get())
        except ValueError:
            messagebox.showerror("Value error", "Price not a float! Taking default value...")
            newPrice = 0
        
        newMovie = Movie(newTitle, newYear, newRating, newActors, newPrice)

        self.movieList.append(newMovie)
        self.listbox.insert(tk.END, str(newMovie))
        self.master.destroy()

class UpdateMovieWindow():

    def __init__(self, master, movieList, listbox):

        #-----<INTERFACE>-----------

        self.movieList = movieList
        self.listbox = listbox
        self.master = master

        self.frame = tk.Frame(master, bd = 20)
        self.frame.pack(side = tk.TOP)

        self.actorsFrame = tk.Frame(master)
        self.actorsFrame.pack(side = tk.BOTTOM)

        self.helpLabel = tk.Label(self.frame, text = "LEAVE BLANK FOR UNCHANGED")
        self.helpLabel.pack(side = tk.TOP)

        self.chooseMovieLabel = tk.Label(self.frame, text = "Choose movie index")
        self.chooseMovieLabel.pack(side = tk.LEFT)
        self.chooseMovieEntry = tk.Entry(self.frame)
        self.chooseMovieEntry.pack(side = tk.LEFT)

        self.titleLabel = tk.Label(self.frame, text = "Title:")
        self.titleLabel.pack(side = tk.LEFT)
        self.titleEntry = tk.Entry(self.frame)
        self.titleEntry.pack(side = tk.LEFT)

        self.yearLabel = tk.Label(self.frame, text = "Year:")
        self.yearLabel.pack(side = tk.LEFT)
        self.yearEntry = tk.Entry(self.frame)
        self.yearEntry.pack(side = tk.LEFT)

        self.ratingLabel = tk.Label(self.frame, text = "Rating:")
        self.ratingLabel.pack(side = tk.LEFT)
        self.ratingEntry = tk.Entry(self.frame)
        self.ratingEntry.pack(side = tk.LEFT)

        self.actorsLabel = tk.Label(self.actorsFrame, text = "Actors (separate by NewLine):")
        self.actorsLabel.pack(side = tk.LEFT)
        self.actorsText = tk.Text(self.actorsFrame)
        self.actorsText.pack(side = tk.LEFT)

        self.priceLabel = tk.Label(self.frame, text = "Price:")
        self.priceLabel.pack(side = tk.LEFT)
        self.priceEntry = tk.Entry(self.frame)
        self.priceEntry.pack(side = tk.LEFT)
        
        self.submitButton = tk.Button(self.actorsFrame, text = "Submit", bg = "grey", command = self.SubmitMovieDetails)
        self.submitButton.pack(side = tk.RIGHT, fill = tk.BOTH)

        #-----</INTERFACE>-----------

    def SubmitMovieDetails(self):

        try:
            movieId = int(self.chooseMovieEntry.get())
            if movieId >= len(self.movieList):
                movieId = len(self.movieList) - 1
            elif movieId < 0:
                movieId = 0

        except ValueError:
            messagebox.showerror("Value error", "ID not an integer!")
            self.master.destroy()
            return

        try: 

            newTitle = self.titleEntry.get()
            if newTitle in ['', None]:
                newTitle = self.movieList[movieId].title

        except ValueError:
            messagebox.showerror("Value error", "Title not a string!")
            newTitle = self.movieList[movieId].title

        try:
            
            if self.ratingEntry.get() in ['', None]:
                newRating = self.movieList[movieId].rating
            else:
                newRating = float(self.ratingEntry.get())
        except ValueError:
            messagebox.showerror("Value error", "Rating not a float! Taking default value...")
            newRating = self.movieList[movieId].rating

        try:
            
            if self.yearEntry.get() in ['', None]:
                newYear = self.movieList[movieId].year
            else:
                newYear = int(self.yearEntry.get())
        except ValueError:
            messagebox.showerror("Value error", "Year not an integer! Taking default value...")
            newYear = self.movieList[movieId].year

        try:
            actorData = self.actorsText.get("1.0",'end-1c')
            newActors = actorData.splitlines()
            if newActors in ['', None]:
                newActors = self.movieList[movieId].actors
        except ValueError:
            messagebox.showerror("Value error", "Actor list not properly defined!")
           
        try: 
            
            if self.priceEntry.get() in ['', None]:
                newPrice = self.movieList[movieId].price
            else:
                newPrice = float(self.priceEntry.get())
        except ValueError:
            messagebox.showerror("Value error", "Price not a float! Taking default value...")
            newPrice = self.movieList[movieId].price

        self.movieList[movieId] = Movie(newTitle, newYear, newRating, newActors, newPrice)
        self.listbox.delete(movieId)
        self.listbox.insert(movieId, str(self.movieList[movieId]))
        self.master.destroy()
