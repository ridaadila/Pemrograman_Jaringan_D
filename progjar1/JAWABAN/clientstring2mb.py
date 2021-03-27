import sys
import socket
import string
import random

ip = ['192.168.122.201','192.168.122.19']

for i in range(2):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (ip[i], 10000)
    print(f"connecting to {server_address}")
    sock.connect(server_address)

    try:
       # Send data
       
       myfile = open('/home/work/Pemrograman_Jaringan_D/progjar1/String2MB.txt', 'r')
       message = ''
       while True:
          char = myfile.read(1)
          if char:
             message +=char
          else:
             break
       myfile.close()
       
       print(f"sending {message}")
       sock.sendall(message.encode())
       print(message.encode())
       # Look for the response
       amount_received = 0
       amount_expected = len(message.encode())
    
       while amount_received < amount_expected:
          data = sock.recv(16)
          amount_received += len(data)
          print(f"{data}")
          print("size of data : ", amount_received)
       
    finally:
      print("closing")
      sock.close()
