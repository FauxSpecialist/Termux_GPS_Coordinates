import socket
import time

host = '192.168.1.73'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen()
print("Listening...")
conn, addr = s.accept()
print(f"Connection: {addr}")
while True:
    data = conn.recv(1024)
    if not data:
        time.sleep(60)
    location  = data.decode()
    print(location)