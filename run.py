#!/usr/bin/env python3.6
from password_locker import User , Credentials
def create_user(fname,lname,password):
    '''
    Function to create new user
    '''
    new_user = User(fname,lname,password)
    return new_user
    
