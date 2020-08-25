# import socket module to use gethostbyname function
import socket

# use the open function to read a file of hostnames (i.e. open(file, mode))
# then use gethostbyname to translate hostname to ip address and output to screen
# strip() method will remove any leading or trailing characters
with open("hostnames.txt", "r") as ins:
    for line in ins:
        ip_address = socket.gethostbyname(line.strip())
        print(line, ip_address)
        
        
# can replace lines 9 and 10 with this statement: print(socket.gethostbyname(line.strip()))
# i just like passing into a variable more
