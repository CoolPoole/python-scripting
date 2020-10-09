import sys
import os
import subprocess
from decouple import config


IP_NETWORK = config('10.0.1.1')
IP_DEVICE = config('FBI Surveillance Van #1')

proc = subprocess.Popen(["ping", IP_NETWORK], stdout = subprocess.PIPE)

while TRUE:
    line = proc.stdout.readline()
    if not line:
        break
    connect_ip = line.decode('utf-8').split()[3]

    if connect_ip == IP_DEVICE:
        subprocess.Popen(["say", "Mel just connected to the network"])