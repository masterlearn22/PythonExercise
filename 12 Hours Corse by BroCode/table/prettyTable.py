from prettytable import PrettyTable

# Data kegiatan
data = [
    ["Sholat Tepat Waktu", "High", "Ibadah"],
    ["Belajar Python", "High", "Belajar"],
    ["Easy Run 5km", "High", "Lari"],
    ["25 Pull Every Day", "High", "Workout"],
    ["Tugas Kuliah", "High", "Tugas, Kuliah"],
    ["Kos Bersih", "High", "Side Quest"],
    ["Push Pull Leg Day", "Medium", "Workout"],
    ["Melihat Podcast", "Low", "Belajar"],
]

# Header tabel
headers = ["No.","Nama Kegiatan", "Prioritas", "Jenis Kegiatan"]

# Membuat tabel menggunakan PrettyTable
table = PrettyTable()
table.field_names = headers

# Menambahkan data ke tabel

with open('table/kegiatan.txt', 'a') as f:
    f.write("\n\nPretty Table\n")
    for index,row in enumerate(data, start=1):
        table.add_row([index] + row)
        
    f.write(str(table) + "\n")
    print("Data Diperbarui")
        
# Menampilkan tabel
# print(table)


