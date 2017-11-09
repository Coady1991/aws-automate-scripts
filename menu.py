#!/usr/bin/python3

# Text menu in Python

import os
# Using the subprocess module to execute a command http://www.sharats.me/posts/the-ever-useful-and-neat-subprocess-module/
import subprocess

# Menu deisgn
def print_menu():
    print (20 * "-", "MENU" , 20 * "-")
    print ("1. Create a New Instance")
    print ("2. Check if Nginx is running")
    print ("3. Create a New Bucket")
    print ("4. Upload a file to a Bucket")
    print ("5. Add file to Index page")
    print ("0. Exit")
    print (46 * "-")

loop = True

# While loop continues until loop = False
while loop:
    # Displays the menu above
    print_menu()
    choice = input("Please select an option: ")

    if choice == "1":
        subprocess.call(['python3', 'run_newwebserver.py'])
        print (5 * '\n')
    elif choice == "2":
        subprocess.call(['python3', 'list_instances.py'])
        print (5 * '\n')
    elif choice == "3":
        subprocess.call(['python3', 'create_bucket.py'])
        print (5 * '\n')
    elif choice == "4":
        subprocess.call(['python3', 'put_bucket.py'])
        print (5 * '\n')
    elif choice == "5":
        subprocess.call(['python3', 'add_file.py'])
        print (5 * '\n')
    elif choice == "0":
        # loop set to False, exits menu
        print("Exiting menu")
        loop = False
    else:
        # Clears the screen and prints an error message for invalid input
        os.system('clear')
        print("That is not an option. Please select again")
