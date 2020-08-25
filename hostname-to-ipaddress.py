import socket

with open("test.txt", "r") as ins;
    for line in ins:
        print socket.gethostbyname(line.strip())
