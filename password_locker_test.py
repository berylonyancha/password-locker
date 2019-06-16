import unittest
from password_locker import User, Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before  each test
        '''
        self.new_user = User("Beryl","Onyancha","skittles")
    def tearDown(self):
        '''
        Tear down method performs clean up after each test method completes
        '''
        User.user_list = []
