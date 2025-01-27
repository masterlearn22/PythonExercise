

def txt():
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
    # print(table)

    text_file="Ini adalah daftar nama orang orang keren"
    namas=["Surya", "Reta","Budi","Yustina","Nara","Mentari","Fajar"]
    file_loc1="files/nama.txt"
    file_loc2="files/infoFiles.txt"
    try:
        with open (file_loc2,"w") as file:
            file.write(str(table))
        print(f"Tabel sudah buat di {file_loc2}")
    except :
        print("Error")
        
    try:
        with open (file_loc1,"w") as file:
            file.write(text_file+"\n")
            for i, nama in enumerate(namas, start=1):  # Gunakan enumerate untuk memberikan nomor urut
                file.write(f"{i}. {nama}\n")  # Format string untuk menambahkan nomor dan nama
            
            print(f"Data telah dibuah di path {file_loc1}")
    except:
        print("File telah dibuat")
        
def json():
    import json
    
    # Membuat data JSON
    data = {
        "nama": "Surya",
        "umur": 20,
        "alamat": "Jl. Dharmawangsa VII",
        "hobi": [
            "Coding", 
            "Lari",
            "Olahraga",
            "Membaca Buku"
        ],
        "kota": "Surabaya",
        "makanan_favorit" : "Pecel"
    }
    
    file_path = "files/informasi.json"
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4) 
            # dump() digunakan untuk menulis atau convert data ke file 
            # indent=4 -> memberikan jarak 4 space untuk membuat format JSON lebih rapi 
            print(f"Data telah dibuat di path {file_path}")
    except:
        print("File telah dibuat")
        
# json()



import csv

def tipe1():
    import csv
    """Membuat CSV menggunakan pendekatan pertama."""
    # Data CSV
    data = {
        "Nama": ["Surya", "Dwi", "Satria"],
        "Umur": [20, 21, 19],
        "Alamat": ["Jl. Dharmawangsa VII", "Jl. Dharmawangsa VIII", "Jl. Dharmawangsa IX"],
        "Hobi": ["Coding", "Lari", "Olahraga"],
        "Kota": ["Surabaya", "Jombang", "Nganjuk"],
        "Makanan_Favorit": ["Pecel", "Gado-Gado", "Sate"],
    }

    file_path = "files/informasi.csv"
    try:
        with open(file_path, mode="a", newline="\n", encoding="utf-8") as f:
            writer = csv.writer(f)
            
            writer.writerow(["\nTipe 1\n"])
            # Menulis header
            header = data.keys()
            writer.writerow(header)
            
            # Menulis isi data
            rows = zip(*data.values())
            writer.writerows(rows)
            
        print(f"Data telah dibuat dengan metode tipe1 di path: {file_path}")
    except Exception as e:
        print(f"Terjadi kesalahan pada tipe1: {e}")

def tipe2():
    import csv
    """Membuat CSV menggunakan pendekatan kedua."""
    # Data CSV
    data = {
        "Nama": ["Surya", "Dwi", "Satria"],
        "Umur": [20, 21, 19],
        "Alamat": ["Jl. Dharmawangsa VII", "Jl. Dharmawangsa VIII", "Jl. Dharmawangsa IX"],
        "Hobi": ["Coding", "Lari", "Olahraga"],
        "Kota": ["Surabaya", "Jombang", "Nganjuk"],
        "Makanan_Favorit": ["Pecel", "Gado-Gado", "Sate"],
    }

    file_path = "files/informasi.csv"
    try:
        with open(file_path, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["\nTipe 2\n"])
            
            # Menulis data sebagai pasangan key-value
            for row in data.items():
                writer.writerow(row)
                
        print(f"Data telah dibuat dengan metode tipe2 di path: {file_path}")
    except Exception as e:
        print(f"Terjadi kesalahan pada tipe2: {e}")

def csv(pilih):
    """Memilih metode pembuatan CSV berdasarkan parameter."""
    if pilih == 1:
        tipe1()
    elif pilih == 2:
        tipe2()
    else:
        print("Pilihan tidak valid! Pilih 1 untuk tipe1 atau 2 untuk tipe2.")

# Contoh pemanggilan fungsi
csv(1)  # Memanggil tipe1
csv(2)  # Memanggil tipe2
