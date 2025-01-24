import os
from prettytable import PrettyTable

# Membuat tabel
table = PrettyTable()
table.field_names = ["Mode", "Deskripsi"]

# Menambahkan data ke tabel
table.add_row(["r", "Membaca file. Error jika file tidak ada."])
table.add_row(["w", "Menulis file. Membuat file baru jika tidak ada. Isi file ditimpa."])
table.add_row(["x", "Membuat file baru. Error jika file sudah ada."])
table.add_row(["a", "Menambahkan data ke file. Membuat file baru jika tidak ada."])
table.add_row(["b", "Mode biner untuk file non-teks."])
table.add_row(["t", "Mode teks untuk file (default)."])
table.add_row(["r+", "Membaca dan menulis file. Error jika file tidak ada."])
table.add_row(["w+", "Menulis dan membaca file. Membuat file baru atau menimpa isi file lama."])
table.add_row(["a+", "Menambahkan data dan membaca file. Membuat file baru jika tidak ada."])

# Cetak tabel
print(table)

text_file="Ini adalah daftar nama orang orang keren"
namas=["Surya", "Reta","Budi","Yustina","Nara","Mentari","Fajar"]
file_name="nama.txt"

try:
    with open (file_name,"w") as file:
        file.write(text_file+"\n")
        for i, nama in enumerate(namas, start=1):  # Gunakan enumerate untuk memberikan nomor urut
            file.write(f"{i}. {nama}\n")  # Format string untuk menambahkan nomor dan nama
        
        print("Data telah ditulis ke file")
except:
    print("File telah dibuat")