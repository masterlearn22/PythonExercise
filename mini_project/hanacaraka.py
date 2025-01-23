# Daftar Hanacaraka (aksara Jawa)
hanacaraka = [
    "ꦲ", "ꦤ", "ꦕ", "ꦫ", "ꦏ", "ꦢ", "ꦠ", "ꦱ", "ꦮ", "ꦭ",
    "ꦥ", "ꦝ", "ꦗ", "ꦪ", "ꦚ", "ꦩ", "ꦒ", "ꦧ", "ꦛ", "ꦔ"
]

# Menambahkan huruf Latin sebagai referensi untuk pencocokan
latin = [
    "A", "na", "ca", "ra", "ka", "da", "ta", "sa", "wa", "la",
    "pa", "dha", "ja", "ya", "nya", "ma", "ga", "ba", "tha", "nga"
]

while True:
    text = input("Masukkan teks yang ingin diubah menjadi Hanacaraka (ketik 'exit' untuk keluar): ").lower()
    if text == "exit":
        break
    
    # Mulai proses konversi
    jawa = ""
    words = text.split()  # Memecah teks berdasarkan spasi
    for word in words:
        for char in word:
            if char in latin:  # Periksa apakah karakter ada di daftar Latin
                index = latin.index(char)
                jawa += hanacaraka[index]  # Tambahkan aksara Jawa sesuai indeks
            else:
                jawa += char  # Jika karakter tidak ditemukan, tetap tambahkan karakter asli
        jawa += " "  # Menambahkan spasi antar kata
    
    print("Hasil konversi teks ke dalam aksara Jawa: ", jawa)
