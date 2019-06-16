import unittest
from password_locker import User, Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Beryl","Onyancha","skittles")