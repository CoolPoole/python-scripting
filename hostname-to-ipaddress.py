# Python script to take hostnames as input and produce their associated IP address(es)
# Author: JustCooLpOOLe
# Version: 1.0
# License: (o^o)

# module import section
import socket
import time
import pyfiglet

# methods section
def single_input():
    single_domain = input("\nPlease enter your domain: ")
    print("\nLooking up", single_domain, "...\n")
    time.sleep(1)

    ip_address = socket.gethostbyname(single_domain)
    print("The IP for", single_domain, "is", ip_address, "\n")

def file_input():
    filename = input("\nPlease enter your filename: ")

    try:
        
        # open() function to read filename variable
        with open(filename, "r") as ins:
            print("\nImporting file(s)...\n")
            time.sleep(3)

            print(" ")

            for line in ins:
                ip_address = socket.gethostbyname(line.strip()) # strip() will strip any trailing or leading blank spaces
                print("The IP for", line, "is", ip_address, "\n")
    except IOError:
        print("\nYour file does not exist. You may need to specify the full path.")

def quitter():
    print("\n--------------------------")
    print("Smell ya later! Closing...")
    print("--------------------------\n")
    time.sleep(3)

# global variable declaration
again = 'Y'

# title header
ascii_banner = pyfiglet.figlet_format("\nLet's Convert Hostnames to IP Addresses!")
print(ascii_banner)

while (again != 'N'):
    
    choice = int(input("\nEnter \n (1) for single domain\n (2) for a file\n (3) to quit \r\n\n Choice: "))

    if (choice == 1):
        single_input()
    elif (choice == 2):
        file_input()
    else:
        quitter()
        break

    again = input("\nWould you like to look up more? (Y/N) ")

else:
    quitter()



              

