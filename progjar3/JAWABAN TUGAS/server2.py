import socket

IP_ADDRESS = '192.168.122.235'
PORT = 5050

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(((IP_ADDRESS,PORT)))

nama_file = ['hasil_metodologi_penelitian.pdf','Hasil_Architecture_Principles.docx']

for i in range(len(nama_file)):
    fp = open(nama_file[i],'wb+')

    while True:
        data, addr = sock.recvfrom(1024)
        print(addr)
        print("diterima ", data)
        print("dikirim oleh ", addr)
        fp.write(data)
    fp.close()

print("closing")
sock.close()