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

def save_password(credentials):
    '''
    Function to save a new credential
    '''
    credentials.save_password(credentials)
def display_passwords():
    '''
    Function to display saved credentials 
    '''
    return Credentials.display_passwords()
def find_site(site):
    '''
    Function that finds a site credentials by site name
    '''
    return Credentials.site_exist(site)
def main():
    print("Hello, Habari. Welcome here.What's your name")
    user_name = input()
    print(f"Hello {user_name}. How may I be of service to you?")
    print('\n')
    while True:
        print("Use these short codes : ca-Create a new user,dc-Display credentials,fs-Find a site, ex-Exit ")
        short_code = input().lower()
if __name__ == '__main__':

    main()