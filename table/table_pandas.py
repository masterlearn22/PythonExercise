import pandas as pd

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

# Tambahkan nomor urut ke data

# Membuat DataFrame dari data
with open ('table/kegiatan.txt','a') as f:
    print("\n\n Pandas Table\n")
    df = str(pd.DataFrame(data, columns=["Nama Kegiatan", "Prioritas", "Jenis Kegiatan"]))
    f.write(df )
    print("Data Diperbarui")

# Menampilkan DataFrame
print(df)
