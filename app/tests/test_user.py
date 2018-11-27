import unittest
from app.models import User

class User(unittest.TestCase):
    '''
    Tests behaviour of the User class
    '''

    def setUp(self):
        '''
        Method that will run before every test
        '''
        