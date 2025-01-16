# Keranjang belanja

food = []
price = []
total = [] 

# Mengumpulkan nama makanan
while True: 
    food_item = input("Masukkan nama makanan (tekan Enter untuk selesai): ")
    if food_item == "":
        break
    food.append(food_item)
    
# Mengumpulkan harga makanan
for item in food: 
    while True:
        try:
            price_item = int(input(f"Masukkan harga untuk {item}: "))
            price.append(price_item)
            break
        except ValueError:
            print("Harga tidak valid. Silakan masukkan angka.")

# Menampilkan daftar makanan dan meminta pembelian
print("\nPilih makanan yang ingin dibeli:")
for i in range(len(food)):
    print(f"{i + 1}. {food[i]} - Rp. {price[i]:,}")

while True:
    try:
        makanan_dibeli = int(input("Masukkan nomor makanan yang ingin dibeli (0 untuk selesai): "))
        if makanan_dibeli == 0:
            break
        if 1 <= makanan_dibeli <= len(food):
            total_item = int(input("Masukkan jumlah makanan yang dibeli: "))
            total_harga = price[makanan_dibeli - 1] * total_item
            total.append(total_harga)
            print(f"Total harga untuk {food[makanan_dibeli - 1]} (jumlah: {total_item}) adalah Rp. {total_harga:,}")
        else:
            print("Nomor makanan tidak valid. Silakan coba lagi.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

# Menghitung total keseluruhan
total_keseluruhan = sum(total)
print(f"\nTotal keseluruhan belanja Anda adalah Rp. {total_keseluruhan:,}")