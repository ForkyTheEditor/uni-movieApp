#THIS IS THE MAIN MODULE; RUN ON START
import pickle
import tkinter as tk
from movieWindowsManager import MovieWindow  
from userWindowsManager import UserWindow
from miscWindowsManager import MiscWindow
from userManager import User
from userManager import UserManager
from moviesManager import Movie
from moviesManager import MovieManager
from miscManager import MiscManager
from testModule import TestClass

class MovieStore:
    """ The main class of the application """

    def main():
        #MAIN FUNCTION OF THE PROGRAM        
        

        movieList = [] #Main movie list of the program
        userList = [] #Main user list of the programs

        movieMaster = tk.Tk()
        movieWindow = MovieWindow(movieMaster, movieList)

        commonMaster = tk.Toplevel()
        commonWindow = MiscWindow(commonMaster, movieList, userList)
        
        userMaster = tk.Toplevel()
        userWindow = UserWindow(userMaster, userList, commonWindow)
        

        shouldExit = False #Set to true to exit loop

        initializationText = """ Hello! What would you like to do?
        User menu:
            1. Add a user
            2. Change a user's name
            3. Remove a user
        Movie menu:
            4. Add a movie
            5. Update a movie's price
            6. List all movies
        Miscellaneous menu:
            7. Order a movie
            8. List user's movie orders
            9. Search movies by rating
            10. Filter movies by actors

            0. Exit program
        """
        
        #Run Unit tests
        TestClass.RunTests()


        #Populate the user list from the database
        try:
            userInfile = open("userDatabase", "rb")
        except:

            print("No user database found!")

        else:
            while True:
            
                try:
                    userList.append(UserManager.DictionaryToUser(pickle.load(userInfile)))
                except:
                    break
        
        #Populate the movie list from the database
        try:
            movieInfile = open("movieDatabase", "rb")
        except:

            print("No movie database found!")

        else:
            while True:
            
                try:
                    movieList.append(MovieManager.DictionaryToMovie(pickle.load(movieInfile)))
                except:
                    break

        #Fill the movie list Widget        
        for movie in movieList:
            movieWindow.list.insert(tk.END, str(movie))

        #Fill the user list Widget        
        for user in userList:
            userWindow.list.insert(tk.END, str(user))
            commonWindow.list.insert(tk.END, str(user))
            

        movieMaster.mainloop()
        
        #Save the users to the database
        userOutfile = open("userDatabase", "wb")

        for user in userList:

            dict = UserManager.UserToDictionary(user)
            pickle.dump(dict, userOutfile)

        userOutfile.close()

        #Save the movies to the database
        movieOutfile = open("movieDatabase", "wb")

        for movie in movieList:

            dict = MovieManager.MovieToDictionary(movie)
            pickle.dump(dict, movieOutfile)

        movieOutfile.close()

        print("Goodbye!")

        #while shouldExit == False:
        #    #MAIN LOOP OF THE PROGRAM
            
        #    #Print the user menu
        #    print(initializationText)
            
        #    ##Update the movie list Widget
        #    #movieWindow.list.delete(0, tk.END)
       
            
            
            
        #    #Get user input
        #    try:
        #        userChoice = int( input("Your choice: ") )
        #    except ValueError:
        #        print("Choice is not an integer!")
        #        continue

        #    if userChoice == 0:
        #        #Exits program

        #        #Save the users to the database
        #        userOutfile = open("userDatabase", "wb")

        #        for user in userList:

        #            dict = UserManager.UserToDictionary(user)
        #            pickle.dump(dict, userOutfile)

        #        userOutfile.close()

        #        #Save the movies to the database
        #        movieOutfile = open("movieDatabase", "wb")

        #        for movie in movieList:

        #            dict = MovieManager.MovieToDictionary(movie)
        #            pickle.dump(dict, movieOutfile)

        #        movieOutfile.close()

        #        print("Goodbye!")
        #        shouldExit = True
        
        #    elif userChoice == 1:
        #        #Add user option
        #        newUser = UserManager.getUserInput()
        #        userList = UserManager.addUser(userList, newUser)         
            
        #    elif userChoice == 2:
        #        #Change a user's name          
        #        userList = UserManager.updateLastname(userList)

        #    elif userChoice == 3:
        #        #Remove a user           
        #        #Check the list isn't empty
        #        if len(userList) == 0:
        
        #            print("The user list is empty!")
        #            continue
                
        #        UserManager.printUsers(userList)

        #        try:
        #            removeUserChoice = int(input("Which user would you like to remove? Index: "))
        #        except ValueError:
        #            print("Choice is not an integer!")
        #            continue

        #        #Clamp the value of the index between the min and the max indexes
        #        if removeUserChoice < 0:
        
        #            removeUserChoice = 0
    
        #        elif removeUserChoice > len(userList) - 1:

        #            removeUserChoice = len(userList) - 1
            
        #        #Remove the selected user
        #        del userList[removeUserChoice]

        #    elif userChoice == 4:
        #        #Add a movie

        #        newMovie = MovieManager.getMovieInput()
        #        movieList = MovieManager.addMovie(movieList, newMovie)
            
        #    elif userChoice == 5:
        #        #Update a movie's price

        #        movieList = MovieManager.updatePrice(movieList)

        #    elif userChoice == 6:
        #        #List all movies
            
        #        MovieManager.printMovies(movieList)

            
        #    elif userChoice == 7:
        #        #Order a movie
            
        #        userList = MiscManager.orderMovies(userList, movieList)

        #    elif userChoice == 8:
        #        #List all user's movie orders
                        
        #        UserManager.printUsers(userList)

        #    elif userChoice == 9:
        #        #Search all movies by rating
            
        #        MiscManager.searchMoviesByRating(movieList)

        #    elif userChoice == 10:
        #        #Filter movies by actors
            
        #        MiscManager.searchMoviesByActor(movieList)
            

if __name__ == "__main__":

    #Run the program
    MovieStore.main()