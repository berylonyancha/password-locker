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
