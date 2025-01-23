import time

def perulangan_angka():
    number = float(input("Masukkan angka: "))  # Menggunakan float untuk mendukung desimal
    loop = int(input("Ulangi berapa kali : "))  
    for x in range(loop):  # Loop sebanyak 10 kali
        for y in range(0, 10):  # Loop untuk menambahkan desimal 
            number += 0.1  # Tambah 0.1 ke number
            print(f"{number:.1f}")  # Cetak angka dengan satu desimal
            time.sleep(0.5) # memberikan jeda output 0.5 detik

    print(f"Angka terakhir: {number:.1f}")

def baris_kolom():
    baris = int(input("Panjang Baris : "))
    kolom = int(input("Panjang kolom : "))
    simbol = input("Masukkan simbol : ")
    for x in range(baris):
        for y in range(kolom):
            print(simbol,end="")
        print() #akan mengeluarkan output kosong sebagai ENTER ketika for loop kedua selesai
    
baris_kolom()
def testing_baris_kolom():
    baris = int(input("Panjang Baris : "))
    kolom = int(input("Panjang kolom : "))
    
    for x in range(kolom):
        print(("*" * baris))
            
# testing_baris_kolom()
    