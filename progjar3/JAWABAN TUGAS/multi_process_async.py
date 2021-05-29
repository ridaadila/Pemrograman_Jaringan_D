# from library import download_gambar, get_url_list
import time
import datetime
from multiprocessing import Process, Pool

import socket

TARGET_IP = "192.168.122.255" #Bcast = Broadcast Address
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)


def kirim_semua():
    texec = dict()
    list_file = ['tes.pdf','tes_progjar.pdf']
    status_task = dict()
    task_pool = Pool(processes=20) #2 task yang dapat dikerjakan secara simultan, dapat diset sesuai jumlah core
    catat_awal = datetime.datetime.now()
    for k in range(len(list_file)):
        print(f"mendownload {list_file[k]}")
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multiprocess
        texec[k] = task_pool.apply_async(func=kirimfile, args=(list_file[k],))

    #setelah menyelesaikan tugasnya, dikembalikan ke main process dengan mengambil hasilnya dengan get
    for k in range(len(list_file)):
        status_task[k]=texec[k].get(timeout=10)

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("status TASK")
    print(status_task)

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

#fungsi download_gambar akan dijalankan secara multi process

if __name__=='__main__':
    kirim_semua()