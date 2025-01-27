from tabulate import tabulate

data= [
    ["Sholat Tepat Waktu","High","Ibadah"],
    ["Belajar Python","High","Belajar"],
    ["Easy Run 5km","High","Lari"],
    ["25 Pull Every Day","High", "Workout"],
    ["Tugas Kuliah","High","Tugas, Kuliah"],
    ["Kos Bersih","High","Side Quest"],
    ["Push Pull Leg Day","Medium","Workout"],
    ["Melihat Podcast","Low","Belajar"]
]

headers = ["No","Nama Kegiatan"," Prioritas","Jenis Kegiatan"]

for i in range(len(data)):
    data[i] = [i+1] +data[i]
    

with open("table/kegiatan.txt", "a") as f:
    f.write("\n\nTabulate Table\n")
    f.write((tabulate(data,headers,tablefmt = "grid")))
    print("Data Diperbarui")
