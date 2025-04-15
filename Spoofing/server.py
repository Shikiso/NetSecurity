import socket

HOST = '0.0.0.0' # IP address that accepts connection from any interface
PORT = 1234
s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
print("Listening for connection...")

while True:
    conn, addr = s.accept()
    print("Connection made!\n", addr)
    conn.close()