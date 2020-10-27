#STACK
tumpukkan_koin = [1000, 500, 100] #menyimpan isian list tumpukkan_koin

def isEmpty(): #fungsi untuk melihat isi data yang ada pada tumpukkan_koin
    print("\n") #untuk memberi jarak dilayar output
    if tumpukkan_koin == []: 
        print("Tidak ada tumpukkan, harap tambahkan terlebih dahulu")

    else:
        print("Tumpukkan uang koin sudah ada :", tumpukkan_koin, ". Tambah kembali")
    #dari baris 5-9 itu untuk mengecek isi data pada list tumpukkan_koin
    #apakah ada isinya atau tidak
    print("\n") #untuk memberi jarak dilayar output
    main() #balik ke fungsi main

def push(): #fungsi untuk menambahkan data pada tumpukkan uang koin
    while True: #melakukan perulangan
        tumpukkan_koin_baru = int(input("Masukkan nilai uang koin : ")) #menginisialisasi variabel baru untuk menginput uang koin
        tumpukkan_koin.append(tumpukkan_koin_baru) #variabel baru untuk menginput uang koin akan ditambahkan kedalam list tumpukkan_koin
        
        print("\nTumpukkan koin: ", tumpukkan_koin) #maka akan menampilkan hasil tumpukkan uang koin yg sudah ditambah datanya
        print("\n") #untuk memberi jarak dilayar output
        main() #balik ke fungsi main
        
def pop(): #untuk menghapus isi data pada tumpukkan_koin
    print("\nTumpukkan uang koin yang dihapus: ", tumpukkan_koin.pop()) #karena stack(LIFO) maka data terakhir yang dihilangkan/hapus
    print("Tumpukkan koin saat ini: ", tumpukkan_koin) #menampilkan hasil tumpukkan uang koin yang sudah dihapus
    print("\n") #untuk memberi jarak dilayar output
    main() #balik ke fungsi main

def size(): #fungsi untuk menghitung banyaknya data yg ada pada tumpukkan_koin
    print("\nBanyaknya Tumpukkan : ", len(tumpukkan_koin)) #menggunakkan len, dan akan menampilkan ke layar
    print("Tumpukkan koin saat ini : ", tumpukkan_koin) #menampilkan tumpukkan uang koin ke layar
    print("\n") #untuk memberi jarak dilayar output
    main() #balik ke fungsi main

def option(pil): #fungsi untuk memilih pada menu
    if pil == "1" : #jika pilihannya nomer 1
        isEmpty() #akan ke fungsi isEmpty
    elif pil == "2": #jika pilihannya nomer 2
       push() #akan ke fungsi push  
    elif pil == "3": #jika pilihannya nomer 3
        pop() #akan ke fungsi pop
    elif pil == "4": #jika pilihannya nomer 4
        size() #akan ke fungsi size

def main(): #fungsi untuk menu utamanya
    while True: #melakukan perulangan
        print("\n#Program implementasi stack menggunakkan list pada Tumpukkan uang koin#\n") #menampilkan ke layar
        print("==========================================") #untuk memberi jarak dilayar output
        print("\nSelamat datang di program Stack uang koin\n") #menampilkan ke layar dan untuk memberi jarak dilayar output
        pilihan = ["1", "2", "3", "4"] #membuat list pilihan
        print ("Pilihan Menu Utama:\n") #menampilkan ke layar
        print (" 1. List Tumpukkan\n 2. Add \n 3. Remove\n 4. Total Tumpukkan\n") #menampilkan ke layar
        pilihan_baru = input("Masukkan pilihan Anda (1/2/3/4): ") #melakukan input dan menampilkan ke layar
        if (pilihan_baru not in pilihan): #jika apa yg dinput tdk ada pada pilihan
            print ("Maaf pilihan Anda tidak ada.") #maka akan menampilkan ke layar
            break #dan program berhenti
        
        option(pilihan_baru) #akan ke fungsi choice

if __name__ == "__main__": #digunakan untuk mengeksekusi beberapa kode, jika file dijalankan secara langsung
    main() #melakukan pemanggilan

#QUEUE
kode_antrian_mcd = [] #menyimpan isian list kode antrian

def isEmpty(): #fungsi untuk melihat isi data yang ada pada kode antrian
    print("\n") #untuk memberi jarak dilayar output
    if kode_antrian_mcd == []: 
        print("Tidak ada Antrian, harap isi data Pemesanan terlebih dahulu")

    else:
        print("Daftar Antrian :", kode_antrian_mcd)
    #dari baris 5-9 itu untuk mengecek isi data pada list kode antrian
    #apakah ada isinya atau tidak
    print("\n") #untuk memberi jarak dilayar output
    main_() #balik ke fungsi main

def enqueue(): #fungsi untuk menambahkan data pada kode antrian
    while True: #melakukan perulangan
        kode_antrian_mcd_baru = int(input("Masukkan kode antrian : ")) #menginisialisasi variabel baru untuk menginput kode antrian
        kode_antrian_mcd.append(kode_antrian_mcd_baru) #variabel baru untuk menginput kode antrian akan ditambahkan kedalam list kode antrian
        
        print("\nAntrian pelanggan: ", kode_antrian_mcd) #maka akan menampilkan hasil tumpukkan uang koin yg sudah ditambah datanya
        print("\n") #untuk memberi jarak dilayar output
        main_() #balik ke fungsi main
        

def dequeue(): #untuk mengeluarkan(remove) isi data pada kode antrian
    print("\nKode Antrian :", kode_antrian_mcd.pop(0), ". Sudah melakukan pembayaran") #karena queue(FIFO) maka data pertama yang harus dihilangkan/hapus
    print("Antrian pelanggan saat ini: ", kode_antrian_mcd) #menampilkan hasil kode antrian yang sudah diremove
    print("\n") #untuk memberi jarak dilayar output
    main_() #balik ke fungsi main

def size(): #fungsi untuk menghitung banyaknya data yg ada pada kode antrian
    print("\nBanyaknya Antrian : ", len(kode_antrian_mcd)) #menggunakkan len, dan akan menampilkan ke layar
    print("Antrian pelanggan saat ini: ", kode_antrian_mcd) #menampilkan kode antrian ke layar
    print("\n") #untuk memberi jarak dilayar output
    main_() #balik ke fungsi main

def option(pil): #fungsi untuk memilih pada menu
    if pil == "1" : #jika pilihannya nomer 1
        isEmpty() #akan ke fungsi isEmpty
    elif pil == "2": #jika pilihannya nomer 2
       enqueue() #akan ke fungsi enqueue  
    elif pil == "3": #jika pilihannya nomer 3
        dequeue() #akan ke fungsi dequeue
    elif pil == "4": #jika pilihannya nomer 4
        size() #akan ke fungsi size

def main_(): #fungsi untuk menu utamanya
    while True: #melakukan perulangan
        print("\n#Program implementasi Queue menggunakkan list pada antrian MCD#\n") #menampilkan ke layar
        print("=====================================") #untuk memberi jarak dilayar output
        print("Selamat Datang di program Queue MCD\n") #menampilkan ke layar dan untuk memberi jarak dilayar output
        pilihan = ["1", "2", "3", "4"] #membuat list pilihan
        print ("Pilihan Menu Utama:\n") #menampilkan ke layar
        print (" 1. Daftar Antrian\n 2. Pemesanan\n 3. Pembayaran\n 4. Jumlah Antrian\n") #menampilkan ke layar
        pilihan_baru = input("Masukkan pilihan Anda (1/2/3/4): ") #melakukan input dan menampilkan ke layar
        if (pilihan_baru not in pilihan): #jika apa yg dinput tdk ada pada pilihan
            print ("Maaf pilihan Anda tidak ada.") #maka akan menampilkan ke layar
            break #dan program berhenti
        
        option(pilihan_baru) #akan ke fungsi choice

if __name__ == "__main__": #digunakan untuk mengeksekusi beberapa kode, jika file dijalankan secara langsung
    main_() #melakukan pemanggilan

#SUMBER :
#diktat dan video ka fauzi
#https://www.geeksforgeeks.org/stack-in-python/
#https://www.geeksforgeeks.org/queue-in-python/