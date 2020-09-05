# Python script to read a list of IP addresses in a text file and output their corresponding hostname if possible
# Author: JustCooLpOOLe
# Version: 1.0
# License: (o^o)

# import socket module to use getfqdn function
import socket

# use the open function to read a file of ip addresses (i.e. open(file, mode))
# then use getfqdn to get fully qualified host name of ip address and output to screen
# strip() method will remove any leading or trailing characters
with open("ipaddresses.txt", "r") as ins:
    for line in ins:
        #hostname = socket.gethostbyaddr(socket.gethostbyname(line.strip()))
        #print(line, hostname)
        hostname = socket.getfqdn(line.strip())
        print(hostname, line)

