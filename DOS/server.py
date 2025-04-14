import socket
from threading import Thread

HOST = '0.0.0.0' # IP address that accepts connection from any interface
PORT = 1234

def run(conn, addr):
    while conn:
        try:
            conn.send(b"Hello, World!")
            print(conn.recv(1024))
        except:
            conn.close()

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
print("Listening for connection...")

while True:
    conn, addr = s.accept()
    Thread(target=run, args=(conn,addr)).start()