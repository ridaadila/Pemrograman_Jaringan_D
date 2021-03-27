import sys
import socket


ip = ['192.168.122.232', '192.168.122.229']

for i in range(2):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (ip[i], 10000)
    print(f"connecting to {server_address}")
    sock.connect(server_address)


    try:
       # Send data
       gambar = open('gambarkucing.jpg', 'rb')
       hasil = gambar.read()
       print("sending gambarkucing"+str(i+1)+".jpg")
       sock.sendall(hasil)

       namafile = 'kucing'+str(i+1)
       responfile = open(namafile+'.jpg', 'wb')

       # Look for the response
       amount_received = 0
       amount_expected = len(hasil)
       while amount_received < amount_expected:
           data = sock.recv(16)
           amount_received += len(data)
           if data:
              responfile.write(data)
           else:
              break
    finally:
       print("closing")
       sock.close()
