def harga_barang(harga,diskon=0,pajak=10): #default value jika saat fungsi dipanggil tidak ada value yang di masukkan
    kopi = harga - (harga * diskon / 100) + (harga * pajak / 100)
    print(f"Harga yang harus dibayar Rp {kopi:,}")
#harga_barang(10000,25)

import time

def hitung(stop,mulai=1): #karena default argumen tidak boleh berada sebelum non-default, maka harus di letakkan di belakang argumen yang tidak memiliki default
    for i in range(mulai,stop+1):
        print(i)
        time.sleep(1)
    print("SELESAI!")
    
hitung(10)