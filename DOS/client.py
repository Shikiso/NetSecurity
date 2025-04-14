import socket, time

HOST = '192.168.0.10' # IPv4 address of host with server
PORT = 1234

s = socket.socket()
s.connect((HOST, PORT))

while s:
    start = time.time()
    print(s.recv(1024))
    s.send(b"Hi there")
    end = time.time()
    print(f"Took {str(end-start)}ms to send and recieve a message.\n")
    time.sleep(3)

s.close()