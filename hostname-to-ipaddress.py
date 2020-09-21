# Python script to read a list of hostnames in a text file and output their corresponding IP addresses
# Author: JustCooLpOOLe
# Version: 1.0
# License: (o^o)

# module import section
import socket
import time

# user input
filename = input("Please enter your filename: ")
print("\nImporting file(s)...\n")
time.sleep(3)

print(" ")

# open() function to read filename variable
with open(filename, "r") as ins:
    for line in ins:
        ip_address = socket.gethostbyname(line.strip()) # strip() will strip any trailing or leading blank spaces
        print("The IP for", line, "is", ip_address)


              

