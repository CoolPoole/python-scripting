# Python script to read a list of hostnames in a text file and output their corresponding IP addresses
# Author: JustCooLpOOLe
# Version: 1.0
# License: (o^o)

# module import section
import socket
import time

# methods section
def single_input():
    single_domain = input("\nPlease enter your domain: ")
    print("\nLooking up", single_domain, "...\n")
    time.sleep(1)

    print(" ")

    ip_address = socket.gethostbyname(single_domain)
    print("The IP for", single_domain, "is", ip_address, "\n")

def file_input():
    filename = input("\nPlease enter your filename: ")
    print("\nImporting file(s)...\n")
    time.sleep(3)

    print(" ")

    # open() function to read filename variable
    with open(filename, "r") as ins:
        for line in ins:
            ip_address = socket.gethostbyname(line.strip()) # strip() will strip any trailing or leading blank spaces
            print("The IP for", line, "is", ip_address, "\n")

def quitter():
    print("\n---------------")
    print("Smell ya later!")
    print("---------------\n")

# user input
choice = int(input("Enter \n (1) for single domain\n (2) for a file\n (3) to quit \r\n\n Choice: "))

if (choice == 1):
    single_input()
elif (choice == 2):
    file_input()
else:
    quitter()



              

