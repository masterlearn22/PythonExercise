import sys

nama = "Surya Dwi Satria"
age = int(input("Masukkan umur anda: "))

point = 0

if age >= 18:
    print("Terverifikasi")
else:
    print('Anda belum cukup umur')
    sys.exit()

money = int(input("Masukkan uang anda: "))
if money >= 6000:
    print("Anda bisa membeli minuman")
else:
    print("Uang anda tidak cukup untuk membeli minuman")
    point += 1 

if money >= 10000:
    print("Anda bisa membeli makanan")
else:
    print("Uang anda tidak cukup untuk membeli makanan")
    point += 1

minuman = {
    "es teh": 5000,
    "es jeruk": 6000,
    "es kelapa": 7000,
    "jus alpukat": 8000
} 

makanan = {
    "bakso": 10000,
    "soto": 15000,
    "nasi goreng": 20000,
    "mie ayam": 12000
}

if point == 2:
    print("Kamu tidak diperbolehkan membeli minuman dan makanan")
    sys.exit()  # Menghentikan program jika tidak diperbolehkan
elif point == 1:
    print("Anda hanya diperbolehkan membeli salah satu.")
elif point == 0:
    print("Anda diperbolehkan membeli minuman dan makanan")

# Fungsi untuk memilih minuman
def pilih_minuman(minuman):
    print("Pilih minuman yang ingin anda beli: ")
    # Menampilkan daftar minuman
    for i, (nama_minuman, harga) in enumerate(minuman.items(), start=1):
        print(f"{i}. {nama_minuman} - {harga}")

    # Meminta input dari pengguna
    pilihan = int(input("Masukkan pilihan minuman (1-4): "))

    # Memeriksa apakah pilihan valid
    if 1 <= pilihan <= len(minuman):
        # Mendapatkan nama dan harga minuman yang dipilih
        minuman_terpilih = list(minuman.keys())[pilihan - 1]
        harga_minuman = minuman[minuman_terpilih]
        print(f"Anda memilih {minuman_terpilih} seharga {harga_minuman}")
        return harga_minuman
    else:
        print("Pilihan minuman tidak valid.")
        return 0  # Mengembalikan 0 jika pilihan tidak valid

# Fungsi untuk memilih makanan
def pilih_makanan(makanan):
    print("Pilih makanan yang ingin anda beli: ")
    # Menampilkan daftar makanan
    for i, (nama_makanan, harga) in enumerate(makanan.items(), start=1):
        print(f"{i}. {nama_makanan} - {harga}")

    # Meminta input dari pengguna
    pilihan = int(input("Masukkan pilihan makanan (1-4): "))

    # Memeriksa apakah pilihan valid
    if 1 <= pilihan <= len(makanan):
        # Mendapatkan nama dan harga makanan yang dipilih
        makanan_terpilih = list(makanan.keys())[pilihan - 1]
        harga_makanan = makanan[makanan_terpilih]
        print(f"Anda memilih {makanan_terpilih} seharga {harga_makanan}")
        return harga_makanan
    else:
        print("Pilihan makanan tidak valid.")
        return 0  # Mengembalikan 0 jika pilihan tidak valid

# Memanggil fungsi untuk memilih minuman dan makanan
harga_minuman = 0
harga_makanan = 0

if point == 1:
    harga_minuman = pilih_minuman(minuman)
elif point == 0:
    harga_minuman = pilih_minuman(minuman)
    harga_makanan = pilih_makanan(makanan)

# Menghitung total harga
total_harga = harga_minuman + harga_makanan
print(f"Total harga yang harus dibayar: {total_harga}")