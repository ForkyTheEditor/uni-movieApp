from userManager import User
from userManager import UserManager
from moviesManager import Movie
from moviesManager import MovieManager

class MiscManager:
    """ Manager object containing functions for organizing User and Movie objects """ 

    def orderMovies(userList, movieList):
        """ Add an order to a user's order list. Print the final price
            In: List of users, List of movies
            Out: List of users """

        localUserList = userList.copy()
        localMovieList = movieList.copy()

        #Check if the lists are empty
        if len(localMovieList) == 0:
        
            print("The movie list is empty!")
            return localUserList

        if len(localUserList) == 0:
            print("The user list is empty!")
            return localUserList

        #USER PART
        UserManager.printUsers(localUserList)

        #Get the user for which to place the order
        while True:
            try:
                userChoice = int(input("Select the user for which to place the order; Index:"))
            except ValueError:
                print("Choice is not an integer!")
            else:
                break
        

        #Clamp the index between the min and max indexes
        if userChoice < 0:
        
            userChoice = 0
    
        elif userChoice > len(localUserList) - 1:

            userChoice = len(localUserList) - 1

        selectedUser = localUserList[userChoice]

        #MOVIE PART
        MovieManager.printMovies(localMovieList)

        totalPrice = 0
        currentOrder = []

        while True:
            try:
                nrOfMovies = int(input("How many movies would you like to order? "))
            except ValueError:
                print("Choice is not an integer!")
            else:
                break
        
    
        for i in range(nrOfMovies):

            while True:
                try:
                    movieIndex = int(input("Which movie would you like to order? Index: "))
                except ValueError:
                    print("Choice is not an integer!")
                else:
                    break
 
            #Clamp the index between the min and max indexes
            if movieIndex < 0:
        
                movieIndex = 0
    
            elif movieIndex > len(localMovieList) - 1:

                movieIndex = len(localMovieList) - 1

            currentOrder.append(localMovieList[movieIndex].title)
            totalPrice += localMovieList[movieIndex].price
    
        userOrders = selectedUser.orders.copy()
        userOrders.append(currentOrder)

        localUserList[userChoice].orders = userOrders

        print("Total price of the order: " + str(totalPrice))

        return localUserList



    def searchMoviesByRating(movieList):
        """ Filter the movie list by rating (returns films with rating greater than the input);
            Displays these movies;
            In: List
            Out: Nothing """ 

        localMovieList = movieList.copy()
        moviesToReturn = []

        #Check if the lists are empty
        if len(localMovieList) == 0:
        
            print("The movie list is empty!")
            return []

        while True:
                    try:
                        inputRating = float(input("Find movies with rating greater than: "))
                    except ValueError:
                        print("Choice is not a float!")
                    else:
                        break

    

        #Run through the movie list and take only the ones you need
        for m in range(len(localMovieList)):

            if localMovieList[m].rating > inputRating:
           
                moviesToReturn.append(localMovieList[m])


        if len(moviesToReturn) == 0:

            print("No movies meet the criteria!")
        
        #Finally, print the movies that meet the criteria
        MovieManager.printMovies(moviesToReturn)

    def searchMoviesByActor(movieList):
        """ Search all the movies an actor has played in; 
            Displays these movies;
            In: List
            Out: Nothing """

        localMovieList = movieList.copy()
        moviesToReturn = []

        #Check if the lists are empty
        if len(localMovieList) == 0:
        
            print("The movie list is empty!")
            return []

        inputActor = input("Find movies the actor has played in; Actor: ")
    

        #Run through the lists and save the right ones in a list
        for m in range(len(localMovieList)):

            for n in range(len(localMovieList[m].actors)):

                if localMovieList[m].actors[n] == inputActor:

                    moviesToReturn.append(localMovieList[m])
                    break
       
        if len(moviesToReturn) == 0:

            print("No movies meet the criteria!")

        #Finally, print the movies that meet the criteria
        MovieManager.printMovies(moviesToReturn)
