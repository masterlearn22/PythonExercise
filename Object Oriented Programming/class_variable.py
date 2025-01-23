class mahasiswa:
    nama = "Universitas Airlangga"
    tahun = int(input('Masukkan Tahun Lulusan: '))
    jumlah_lulusan = 0
    
    def __init__(self, nama, tahun):
        self.nama = nama
        self.tahun = tahun
        if self.tahun <= mahasiswa.tahun and self.tahun >= (mahasiswa.tahun-4): 
            mahasiswa.jumlah_lulusan += 1
            
    def info(self):
        print('Nama:', self.nama)
        print('Tahun:', self.tahun)
    
    def info_univ(self):
        print('Nama Universitas:', mahasiswa.nama)
        print('Tahun Universitas:', mahasiswa.tahun)
        print('Jumlah Lulusan:', mahasiswa.jumlah_lulusan)
        
mahasiswa1 = mahasiswa('Surya', 2024)
mahasiswa2 = mahasiswa('Reta', 2023)
mahasiswa3 = mahasiswa('Rudi', 2022)
mahasiswa4 = mahasiswa('Joko', 2021)
mahasiswa5 = mahasiswa('Andi', 2025)
mahasiswa6 = mahasiswa('Riga', 2026)
mahasiswa7 = mahasiswa('Safa', 2020)
mahasiswa8 = mahasiswa('Dewi', 2019)
mahasiswa9 = mahasiswa('Vino', 2020)

print(f"Daftar lulusan dari tahun {mahasiswa.tahun-4} - {mahasiswa.tahun} adalah:\n ")
for mahasiswa_obj in [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4, mahasiswa5, mahasiswa6, mahasiswa7, mahasiswa8, mahasiswa9]:
    if mahasiswa.tahun - 4 <= mahasiswa_obj.tahun <= mahasiswa.tahun:
        mahasiswa_obj.info()
        print()
    

print(f"Jumlah lulusan dari {mahasiswa.nama} adalah {mahasiswa.jumlah_lulusan}")
if mahasiswa.jumlah_lulusan >= 5:
    print('Universitas Airlangga adalah universitas terbaik')
else:
    print('Universitas Airlangga adalah universitas biasa')

        

