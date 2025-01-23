#● ┌ ─ ┐ │ └ ┘

jumlah = int(input("Jumlah data yang ingin diinputkan: "))
kotak_per_baris = 9  # Jumlah kotak maksimum per baris

# List untuk menyimpan baris-baris dari kotak
baris_atas = []
baris_tengah = []
baris_bawah = []

# Loop untuk setiap angka
for i in range(1, jumlah + 1):
    panjang_angka = len(str(i))  # Hitung panjang angka, misal i = 9-> len(str(9))=1 & len(str(10))= 2 & len(str(100))=3
    lebar = panjang_angka + 4  # Tambahkan padding untuk kotak

    # Tambahkan bagian kotak ke string sementara
    baris_atas.append("┌" + "─" * lebar + "┐")
    baris_tengah.append(f"│  {i}  │")
    baris_bawah.append("└" + "─" * lebar + "┘")

    # Jika mencapai jumlah maksimum per baris, cetak dan reset list
    if i % kotak_per_baris == 0 or i == jumlah:
        print("  ".join(baris_atas))  # Gabungkan semua bagian atas
        print("  ".join(baris_tengah))  # Gabungkan semua bagian tengah
        print("  ".join(baris_bawah))  # Gabungkan semua bagian bawah
        # Reset untuk baris berikutnya
        baris_atas.clear()
        baris_tengah.clear()
        baris_bawah.clear()
