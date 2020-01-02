
class Movie:
    """ Generic movie object 
        Attributes: title (string), year (int), rating (float), actors (list), price (float) """

    def __init__(self, title, year, rating, actors, price):
        
        self.__title = title
        try: 
            self.__year = int(year)
        except ValueError: 
            print("Year is not an integer!")

        try:
            self.__rating = float(rating)
        except ValueError:
            print("Rating is not a float!")

        self.__actors = actors
        try:
            self.__price = float(price)
        except ValueError:
            print("Price is not a float!")

        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, newTitle):
        self.__title = newTitle

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, newYear):
        try:
            self.__year = int(newYear)
        except ValueError:
            print("Year is not an integer!")
            self.__year = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, newRating):
        try:
            self.__rating = float(newRating)
        except ValueError:
            print("Rating is not a float!")
            self.__rating = 0

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, newActors):
        self.__actors = newActors

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, newPrice):
        try:
            self.__price = float(newPrice)
        except ValueError:
            print("Price is not a float!")
            self.__price = 0

    def __str__(self):
        return "{self.title} ({self.year}) Rat: {self.rating} Price: {self.price} ".format(self=self) + str(self.actors) 


class MovieManager:
    """ Manager object containing functions for organizing movies """ 

    def getMovieInput():
        """ Takes the user input and converts it to a Movie object 
            In: Nothing
            Out: Movie object"""

        title = input("Movie's title: ")
        while True:
            try:
                year = int( input("Year of release: ") )
            except ValueError:
                print("Choice is not an integer!")
            else:
                break
        while True:
            try:
                rating = float(input("Rating: "))
            except ValueError:
                print("Choice is not a float!")
            else:
                break
        
        actors = []
        while True:
            try:
                iter = int( input("Number of actors you wish to input: ") )
            except ValueError:
                print("Choice is not an integer!")
            else:
                break
        


        for n in range(iter):

            actors.append(input("Actor: "))

        while True:
            try:
                price = float(input("Price: "))
            except ValueError:
                print("Choice is not a float!")
            else:
                break

        newMovie = Movie(title, year, rating, actors, price)

        return newMovie
    
    def addMovie(list, movie):
        """ Add a movie to the movie list;
            In: List, Movie object
            Out: List """
    
        localList = list.copy()    
        localList.append(movie)

        return localList

    def printMovies(list):
        """ Prints the movies in a readable format with indexes;
            In: List
            Out: Nothing """


        for movie in list:
            
            print(str(list.index(movie)) + '.' , movie)


    def updatePrice(list):
        """ Update the price of a movie; Handles user console input
            In: List
            Out: List"""

        localList = list.copy()

        #Check the list isn't empty
        if len(localList) == 0:
        
            print("The movie list is empty!")
            return []

    
        MovieManager.printMovies(localList)

        while True:
            try:
                choice = int(input("Which movie's price would you like to update? Index: "))
            except ValueError:
                print("Choice is not an integer!")
            else:
                break

        while True:
            try:
                newPrice = float(input("The movie's updated price: "))
            except ValueError:
                print("Choice is not a float!")
            else:
                break
        

         #Clamp the value of the index between the min and the max indexes
        if choice < 0:
        
            choice = 0
    
        elif choice > len(localList) - 1:

            choice = len(localList) - 1

        localList[choice].price = newPrice

        return localList

    def MovieToDictionary(movie):
        """ Transforms a movie object into a dictionary to prepare for serialization 
            In: Movie object
            Out: Dictionary """

        if isinstance(movie, Movie):

            movieDict = {'title' : movie.title, 'year' : movie.year, 'rating' : movie.rating, 'actors' : movie.actors, 'price' : movie.price }
            return movieDict
        else:
            return {}

    def DictionaryToMovie(movieDict):
        """ Transforms a dictionary into a movie object after deserialization 
            In: Dictionary
            Out: Movie object """

        movie = Movie(movieDict['title'], movieDict['year'], movieDict['rating'], movieDict['actors'], movieDict['price'] )

        return movie





