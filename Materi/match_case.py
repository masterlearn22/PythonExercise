def nama_nama_hari(hari):
    if hari == 1:
        return "Senin"
    elif hari == 2:
        return "Selasa"
    elif hari == 3:
        return "Rabu"
    elif hari == 4:
        return "Kamis"
    elif hari == 5:
        return "Jumat"
    elif hari == 6:
        return "Sabtu"
    elif hari == 7:
        return "Minggu"
    else: 
        print("Tidak ada")
        

nama_hari = nama_nama_hari(int(input("Hari apa : ")))
print(nama_hari) 

def nama_nama_bulan(bulan):
    if bulan == "1" or bulan == "01":
        return "Januari"
    elif bulan == "2" or bulan == "02":
        return "Februari"
    elif bulan == "3" or bulan == "03":
        return "Maret"
    elif bulan == "4" or bulan == "04":
        return "April"
    elif bulan == "5" or bulan == "05":
        return "Mei"
    elif bulan == "6" or bulan == "06":
        return "Juni"
    elif bulan == "7" or bulan == "07":
        return "Juli"
    elif bulan == "8" or bulan == "08":
        return "Agustus"
    elif bulan == "9" or bulan == "09":
        return "September"
    elif bulan == "10":
        return "Oktober"
    elif bulan == "11":
        return "November"
    elif bulan == "12":
        return "Desember"
    else:
        return "Tidak ada bulan dengan nomor tersebut."
        
# Input bulan
nama_bulan = nama_nama_bulan(input("Masukkan nomor bulan (1-12): "))
print(nama_bulan)

        
nama_bulan = nama_nama_bulan(input("bulan apa : "))
print(nama_bulan) 