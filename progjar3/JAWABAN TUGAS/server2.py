import socket
import sys

IP_ADDRESS = '192.168.122.48'
PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

sock.bind(("", PORT))

#sock.bind(((IP_ADDRESS,PORT)))
count = random.randint(0,3)
fp = open("hasil"+str(count)+".jpg", 'wb')
while True:
    data, addr = sock.recvfrom(1024)
    print(addr)
    print("diterima ", data)
    print("dikirim oleh ", addr)

    fp.write(data)

