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
    def test__init__(self):
        '''
        Test to check if initialization has been done
        ''' 
        self.assertEqual(self.new_credentials.site,"Snapchat")
        self.assertEqual(self.new_credentials.user_name,"Berylzz")
        self.assertEqual(self.new_credentials.password,"1234")

    def test_save_passwords(self):
        '''
        Test to check if the new credential info is saved into the credentials list
        '''
        self.new_credentials.save_password()
        self.assertEqual(len(Credentials.passwords), 1)
    def test_find_site(self):
        '''
        Test to check if the find_site methods returns the correct credentials
        '''
        self.new_credentials.save_password()
        snapchat = Credentials("snapchat","Berylzz","1234")
        snapchat.save_password()
        credential_exists = (Credentials.find_site('snapchat'))
        self.assertEqual(credential_exists, snapchat)
    def test_display_credentials(self):
        '''
        Test to check if the display credentials methods displays all saved credentials
        '''
        self.new_credentials.save_password()
        twitter = Credentials('Twitter', 'berrypondis', '12345')
        twitter.save_password()
        gmail = Credentials('Gmail', 'hoodrat', '123456')
        gmail.save_password()
        self.assertEqual(
        len(Credentials.display_passwords()), 3)   
  
if __name__ =='__main__':
    unittest.main()
