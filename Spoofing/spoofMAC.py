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