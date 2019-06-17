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
    def test_save_user(self):
        '''
        Test to check if users are added to the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    def test_delete_user(self):
        '''
        Test to check if users can be deleted from the users list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","1234")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before  each test
        '''
        self.new_credentials = Credentials("Snapchat","Berylzz","1234")
    def tearDown(self):
        '''
         Tear down method performs clean up after each test method completes
        '''
        Credentials.passwords = []
        