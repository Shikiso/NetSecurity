'''
When testing this out use wireshark to see the packets and watch how the IP
is what you set he SRC_IP to be.
'''

from scapy.all import IP, TCP, send
import random

SRC_IP = '192.168.0.1' # IP that you want to pretend to be
DST_IP = '192.168.0.88' # Server IP address

DST_PORT = 1234 # Port open on server
SRC_PORT = random.randint(1024, 65535) # source ports are random but cannot be the same

ip = IP(src=SRC_IP, dst=DST_IP, frag=0) # Creating the IP packet

# Creating a basic SYN segment
# flags='S' is telling the server the server we send this to that its a syn request
syn = TCP(sport=SRC_PORT, dport=DST_PORT, flags='S')
send(ip/syn) # Sending packet