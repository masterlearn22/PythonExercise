makanan ={
    "Pecel" : 8000,
    "Nasi goreng" : 10000,
    "Rujak" : 7000,
    "Soto": 15000,
    "Rawon": 12000,
}

minuman = {
    "Jus buah" : 5000,
    "Kopi" : 3000,
    "Teh" : 2000, 
    "Smothie" :12000
}

cart=[]
total=0
print("------Daftar makanan------")
for key, values in makanan.items():
    print(f"{key:13} : Rp {values:,}")
print("--------------------------")
  
print("\n------Daftar Minuman------")  
for key, values in minuman.items():
    print(f"{key:13} : Rp {values:,}")
print("--------------------------")

while True:
    while True:
        
        pilih_makanan = input("Masukkan makanan yang ingin dibeli (atau 'q' untuk selesai): ").capitalize()
        if pilih_makanan == 'Q':
            break
        if makanan.get(pilih_makanan): #cara 1
            cart.append(pilih_makanan)
            total += makanan[pilih_makanan]
        else:
            print("Makanan tidak tersedia.")
        
    while True:
        pilih_minuman = input("Masukkan minuman yang ingin dibeli (atau 'q' untuk selesai): ").capitalize()
        if pilih_minuman == 'Q':
            break
        if pilih_minuman in minuman: #cara 2
            cart.append(pilih_minuman)
            total += minuman[pilih_minuman]
        else:
            print("Minuman tidak tersedia.")
    break
    
print("\n---------Pesanan---------")
for item in cart:
    if item in makanan:
        print(f"{item:13} : Rp {makanan[item]:,}")
    elif item in minuman:
        print(f"{item:13} : Rp {minuman[item]:,}")
print("-------------------------")

print(f"{'Total':13} : Rp {total:,}")
