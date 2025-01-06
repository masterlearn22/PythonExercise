nama = input("Masukkan nama Anda: ")
uang = float(input("Masukkan jumlah uang Anda: "))

print(f"Halo, {nama}!")
print("Selamat datang di Wahana bermain City Mall.")

harga_tiket = 30000

while True:
    if uang >= harga_tiket:
        jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
        total = jumlah_tiket * harga_tiket
        
        if total > uang:
            print("Uang Anda tidak cukup untuk membeli tiket tersebut.")
            kurang = total - uang
            print(f"Uang Anda kurang Rp{kurang}")
        else:
            kembalian = uang - total
            print(f"Total harga yang harus dibayar: Rp{total}")
            print(f"Kembalian Anda: Rp{kembalian}")
            break
    else:
        print("Uang Anda tidak cukup untuk membeli tiket.")
        break