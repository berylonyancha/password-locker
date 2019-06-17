#!/usr/bin/env python3.6
from password_locker import User , Credentials
def create_user(fname,lname,password):
    '''
    Function to create new user
    '''
    new_user = User(fname,lname,password)
    return new_user
def save_user(user): 
    '''
    Function to save user
    '''
    user.save_user() 
def create_credential(site,user_name,password):
    '''
	  Function to create a new credential
    '''
    new_credentials=Credentials(site,user_name,password)
    return new_credentials 

