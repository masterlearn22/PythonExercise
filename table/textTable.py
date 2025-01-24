from texttable import Texttable

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

# Membuat tabel menggunakan Texttable
table = Texttable()
table.header(["No.", "Nama Kegiatan", "Prioritas", "Jenis Kegiatan"])

# Menambahkan data ke tabel
for i, row in enumerate(data, 1):
    table.add_row([i] + row)

# Menulis tabel ke file
with open('table/kegiatan.txt', 'a') as f:
    f.write("\n\nText Table\n")
    f.write(table.draw())  # Menggunakan draw() untuk mendapatkan string tabel
    f.write("\n")  # Menambahkan baris baru setelah tabel

print("Data telah disimpan ke file 'kegiatan.txt'")
