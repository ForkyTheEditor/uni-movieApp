from moviesManager import Movie
from moviesManager import MovieManager
from userManager import User
from userManager import UserManager


class TestClass:
    """ Class containing the unit test functions """


    def test_AddMovie():
        """ Unit test for addMovie function """

        newMov = Movie("eaf", 1234, 9, ["blaer"], 493)
        list = []

        list = MovieManager.addMovie(list, newMov)

        assert len(list) == 1

    def test_AddUser():
        """ Unit test for addUser function """

        newUser = User("eaf", "foperski", ["fea"])
        list = []

        list = UserManager.addUser(list, newUser)

        assert len(list) == 1

    def test_UserDict():
        """ Unit test for UserToDictionary function """

        newUser = User("beaf;o", "test", ["koidw"])

        dict = UserManager.UserToDictionary(newUser)

        assert dict['lastName'] == "test"

    def test_DictUser():
        """ Unit test for DictionaryToUser function """

        dict = {'firstName' : 'test', 'lastName' : '[pew', 'orders' : ['wdav']}


        user = UserManager.DictionaryToUser(dict)

        assert user.firstName == "test"

    def RunTests():
        """ Function calling all other test functions
            Add test functions here to call them """

        TestClass.test_AddMovie()
        TestClass.test_AddUser()
        TestClass.test_UserDict()
        TestClass.test_DictUser()
