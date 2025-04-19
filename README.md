# NetSecurity
## I AM NOT RESPONSIBLE FOR ANYONE WHO USES THE CONTENT MALICIOUSLY THIS IS PURELY FOR EDUCATION!!!

## Password Cracking
### Brute Force
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

## Sniffers
Sniffers are tools or devices that sniff packets in the network.
They can be used to see who is sending what where with what information.
Wireshark is problery the most popular and used. Sniffers can be used in
Man-In-The-Middle attacks if something like arp spoofing (mac spoofing) is used along side it.
I haven't made anything for sniffers since I think wireshark is good enough
to use and there is plenty of information online about how to use it.

## Buffer Overflow
A buffer overflow is when an attacker overflows the stack in order to call a function or get a shell.
This is done by supplying more data than there is memory. For example if you have a variable called name
which holds 16 bytes, and 32 bytes are stored in the variable. The 16 bytes that cannot be stored will
overwrite memory in the stack. It's like pouring 1L of water into a 600ml cup. This attack can be
done over a network or on a program on your machine. For this example I used a CTF that runs
on your machine (needs to be linux). Intructions to follow along are in the folder, I'm not going over
assembly, GDB or how anything works just the process of how to complete the CTF. To learn I recommend
these:
**https://www.youtube.com/watch?v=6sUd3AA7Q50&t=1199s&ab_channel=crow**
**https://insecure.org/stf/smashstack.html**
**https://www.youtube.com/watch?v=-iRG9_zFRC4&list=PL1H1sBF1VAKUBfdObXv_MeS4s3n8qwgeU&ab_channel=JohnHammond**
