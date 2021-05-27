import socket
import sys

IP_ADDRESS = '192.168.122.48'
PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

sock.bind(("", PORT))

#sock.bind(((IP_ADDRESS,PORT)))

nama_file = ['hasil_tes.docx','hasil_tes_progjar.pdf']

for i in range(len(nama_file)):
    fp = open(nama_file[i],'w')

    while True:
        data, addr = sock.recvfrom(1024)
        print(addr)
        print("diterima ", data)
        print("dikirim oleh ", addr)
        if(data):
          fp.write(data)
        else:
          fp.close()
          break

print("closing")
sock.close()
