# from library import download_gambar,get_url_list
import time
import datetime
import concurrent.futures
import socket

TARGET_IP = "192.168.122.255" #Bcast = Broadcast Address
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)


def kirim_semua():
    texec = dict()
    list_file = ['metodologi_penelitian.pdf','Architecture_Principles.docx']
    status_task = dict()
    task = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    catat_awal = datetime.datetime.now()
    for k in range(len(list_file)):
        print(f"mendownload {list_file[k]}")
        waktu = time.time()
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multithread
        texec[k] = task.submit(kirimfile, list_file[k])

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan memanggil result
    for k in range(len(list_file)):
        status_task[k]=texec[k].result()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("hasil task yang dijalankan")
    print(status_task)

def kirimfile(list_file=0):
    if(list_file==0):
        print("Tidak ada file")
        exit(1)
    file = open(list_file, 'rb')
    hasil = file.read()
    terkirim = 0
    for x in hasil:
        k_bytes = bytes([x])
        sock.sendto(k_bytes, (TARGET_IP, TARGET_PORT))
        terkirim = terkirim + 1

#fungsi kirim file akan dijalankan secara multithreading

if __name__=='__main__':
    kirim_semua()