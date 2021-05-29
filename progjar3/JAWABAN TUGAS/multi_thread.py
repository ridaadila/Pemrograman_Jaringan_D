# from library import download_gambar,get_url_list
import time
import datetime
import threading
import socket

TARGET_IP = "192.168.122.255" #Bcast = Broadcast Address
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

def kirim_semua():
    texec = dict()
    list_file = ['tes.pdf','tes_progjar.pdf']

    catat_awal = datetime.datetime.now()
    for k in range(len(list_file)):
        print("Mengirim file ", list_file[k])
        waktu = time.time()
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi kirim gambar secara multithread
        texec[k] = threading.Thread(target=kirimfile, args=(list_file[k],))
        texec[k].start()

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan join
    for k in range(len(list_file)):
        texec[k].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


def kirimfile(list_file=0):
    if(list_file==0):
        print("Tidak ada file")
        exit(1)
    file = open(list_file, 'r')
    hasil = file.read()
    terkirim = 0
    for x in hasil:
        k_bytes = bytes([x])
        sock.sendto(k_bytes, (TARGET_IP, TARGET_PORT))
        terkirim = terkirim + 1


#fungsi download_gambar akan dijalankan secara multithreading

if __name__=='__main__':
    kirim_semua()