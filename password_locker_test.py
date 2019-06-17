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
    def test_init(self):
        '''
        Test to check if initialization has been done
        ''' 
        self.assertEqual(self.new_user.first_name,"Beryl")
        self.assertEqual(self.new_user.last_name,"Onyancha")
        self.assertEqual(self.new_user.password,"skittles")
