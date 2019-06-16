class User:
    '''
    class to create user information
    '''
    user_list = []
    def __init__(self, first_name, last_name,password):
        '''
        function to hold user properties
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password 
    def save_user(self):
        '''
        function to save user
        '''    
        User.user_list.append(self)
    def delete_user(self):
        '''
        function to delete user
        '''
        User.user_list.remove(self)
class Credentials:  
    '''
    Class to create and store the user credentials for a new site
    '''
    passwords = []
    def __init__(self,site,user_name,password):
        '''
        Function to create password for a new site
        '''
        self.site = site
        self.user_name = user_name
        self.password = password
    def save_password(self):
        '''
        Saves passwords
        '''
        Credentials.passwords.append(self)
    @classmethod
    def display_passwords(cls):
        '''
        Display saved passwords
        '''
        return cls.passwords
    @classmethod
    def find_site(cls):
        '''
        Method that checks for a site and its credentials
        '''
        for credentials in cls.passwords:
            if credentials.site == site
                return credentials






        
