import os

network_address = '192.168.0.0'

for i in range(1, 255):
    address = network_address[:-1]
    address += str(i)
    os.system("sudo arp -d " + address)