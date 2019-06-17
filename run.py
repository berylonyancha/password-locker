#!/usr/bin/env python3.6
from password_locker import User, Credentials


def create_user(fname, lname, password):
    '''
    Function to create new user
    '''
    new_user = User(fname, lname, password)
    return new_user


def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()


def create_credential(site, user_name, password):
    '''
          Function to create a new credential
    '''
    new_credentials = Credentials(site, user_name, password)
    return new_credentials


def save_password(Credentials):
    '''
    Function to save a new credential
    '''
    Credentials.save_password()


def display_passwords():
    '''
    Function to display saved credentials 
    '''
    return Credentials.display_passwords()


def find_site(site):
    '''
    Function that finds a site credentials by site name
    '''
    return Credentials.find_site(site)


def main():
    print("Hello, Habari. Welcome here.What's your name")
    user_name = input()
    print(f"Hello {user_name}. How may I be of service to you?")
    print('\n')
    while True:
        print("Use these short codes : cc-Create a new credentials,dc-Display credentials,fs-Find a site, ex-Exit ")
        short_code = input().lower()
        if short_code == 'cc':
            print("New Credentials")
            print("-"*10)
            print("Site Name...")
            site = input()
            print("User name...")
            user_name = input()
            print("Enter password for the account")
            password = input()
            save_password(create_credential(site, user_name, password))
            print('\n')
            print(f"New site {site} for {user_name} created")
            print('\n')
        elif short_code == 'dc':
            if display_passwords():
                print("Here is a list of saved credentials")
                print('\n')
                for credentials in display_passwords():
                    print(
                        f"{credentials.site}  {credentials.user_name}.....{credentials.password}")
                    print('\n')
            else:
                    print('\n')
                    print("You dont have anything saved")
                    print('\n')
        elif short_code == 'fs':
            print("Enter the site you want to search for")
            search_site = input()
            if find_site(search_site):
                search_site = find_site(search_site)
                print(
                    f"{search_site.site}  {search_site.user_name}{search_site.password}")
            else:
                print("That site does not exist")
        elif short_code == 'ex':
            print("Bye Kwaheri")
            break
        else:
            print("Oops wrong input. Please use shirtg codes provided")


if __name__ == '__main__':
  main()
