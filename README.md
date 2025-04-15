# NetSecurity
## I AM NOT RESPONSIBLE FOR ANYONE WHO USES THE CONTENT MALICIOUSLY THIS IS PURELY FOR EDUCATION!!!

## Password Cracking
### Brute Foce
Brute force attacks use the computers resources to test
the users password against every combination. These attacks can
take very long if the password is long and complicated.

### Dictionary Attack
A dictionary attack uses a list of common passwords (many are
available online) to guess the users password. A common lists
is the RockYou.txt. However many companies also use these lists
to disallow certain passwords.

### Rainbow Table
A rainbow table is very similar to a dictionary attack
however is uses a precompiles list of passwords with their
plain text version along side them. This makes this attack
must faster than a dictionary since it doesn't need to waste
time hashing the password.

## DOS
A denail of service attack is commonly used to distrupt the flow
of data being sent and recieved or stopping this flow entirely.
A distrubuted denail of service or (DDOS) completes the same attack
but multiple machines (usually a botnet) attack the host or server.
This attack involves sending a large amount of packets to the server or host
to increase the time it takes to interact with clients or crashing the
server or host entirely so that it cannot be used.

## Spoofing
### IP
IP spoofing is when an attacker changes the ip header in a packet to
so that the packet looks like it's comming from a different device.
This is commonly used in SYN DOS attacks.
(Use wireshark to see the packets with the altered source IP)

### MAC
MAC spoofing is the same principle of IP spoofing where the attacker
changes their MAC address to look like a different device. However it
is done differently. For MAC spoofing you'll need to manipulate the ARP
table in devices. This isn't so hard as all devices will send out ARP requests
trying to find a MAC address for a host using a IP address. To spoof your MAC
address simply send out ARP response packets to the target that say you are
a different device for exmaple the default gateway.
I recommend having a look at **https://github.com/davidlares/arp-spoofing/tree/master**
since this helped me with trying to create the script.