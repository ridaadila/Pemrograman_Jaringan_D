import socket
import sys

IP_ADDRESS = '192.168.122.48'
PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

sock.bind(("", PORT))

nama_file = ['hasil1.jpg','hasil2.jpg']
count = 0
while True:
    data, addr = sock.recvfrom(1024)
    print(addr)
    print("diterima ", data)
    print("dikirim oleh ", addr)
    fp = open(nama_file[count], 'wb')
    fp.write(data)
    count+=1

