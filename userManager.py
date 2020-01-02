
class User:
    """ Generic user object 
        Attributes: firstName (string), lastName (string), orders (list) """

    def __init__(self, firstName, lastName, orders):
        
        self.__firstName = firstName
        self.__lastName = lastName
        self.__orders = orders

    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, newName):
        self.__firstName = newName

    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, newName):
        self.__lastName = newName

    @property
    def orders(self):
        return self.__orders

    @orders.setter
    def orders(self, newOrder):
        self.__orders = newOrder


    def __str__(self):
        return  "{self.firstName} {self.lastName}'s orders: ".format(self=self) + str(self.orders)

class UserManager:
    """ Manager object containing functions for organizing users """
    
    def getUserInput():
        """ Takes the user input and converts it to a User object 
            In: Nothing
            Out: User object """

        firstName = input("User's first name: ")
        lastName = input("User's last name: ")
        orders = []
        while True:
            try:
                iterOrd = int(input("Number of orders you wish to input: "))
            except ValueError:
                print("Choice is not an integer!")
            else:
                break
        
        for n in range(iterOrd):

            while True:
                try:
                    iterFilms = int(input("Number of films in order: "))
                except ValueError:
                    print("Choice is not an integer!")
                else:
                    break

            individualOrder = []

            for m in range (iterFilms):

                film = input("Film ordered: ")
                individualOrder.append(film)

            orders.append(individualOrder)

        newUser = User(firstName, lastName, orders)

        return newUser

    def addUser(list, user):
        """ Add a User to the user list;
            In: List, User object
            Out: List """

        localList = list.copy()
        localList.append(user)

        return localList

    def printUsers(list):
        """ Prints the users in a readable format with indexes;
            In: List
            Out: Nothing """


        for user in list:
            
            print(str(list.index(user)) + '.' , user)


    def updateLastname(list):
        """ Update the last name of a user; Handles user console input
            In: List
            Out: List"""

        localList = list.copy()

        #Check the list isn't empty
        if len(localList) == 0:
        
            print("The user list is empty!")
            return []

        UserManager.printUsers(localList)
        
        while True:
            try:
                choice = int(input("Which user's last name would you like to update? Index: "))
            except ValueError:
                print("Value is not an integer!")
            else:
                break

        newName = input("The user's updated last name: ")


         #Clamp the value of the index between the min and the max indexes
        if choice < 0:
        
            choice = 0
    
        elif choice > len(localList) - 1:

            choice = len(localList) - 1


        localList[choice].lastName = newName

        return localList
    
    def UserToDictionary(user):
        """ Transforms a user object into a dictionary to prepare for serialization 
            In: User object
            Out: Dictionary """

        if isinstance(user, User):

            userDict = { 'firstName' : user.firstName, 'lastName' : user.lastName, 'orders' : user.orders}

            return userDict

        else:
            
            return {}

    def DictionaryToUser(userDict):
        """ Transforms a dictionary into a user object after deserialization 
            In: Dictionary
            Out: User object """

        user = User(userDict['firstName'], userDict['lastName'], userDict['orders'])

        return user



