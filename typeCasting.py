
nama = "Surya Dwi Satria"
umur = 20
tinggi = 183.5
berat = 70
mahasiswa = True

#untuk mengetahui tipe data dari variabel
print(type(nama)) #str
print(type(umur)) #int
print(type(tinggi)) #float
print(type(berat)) #int

#mengubah tipe data
nama =bool(not(nama))   #mengubah tipe data str ke bool dan membuat nilai menjadi False, 
                        #jika ingin mengubah menjadi True maka harus menggunakan not() lagi atau menghapus not() pada kode
umur = str(umur) #mengubah tipe data int ke str
tinggi = int(tinggi) #mengubah tipe data float ke int
berat = float(berat) #mengubah tipe data int ke float
mahasiswa = str(mahasiswa) #mengubah tipe data bool ke str

print(type(umur)) 
print(type(tinggi))
print(type(berat))
print(type(mahasiswa))
print(mahasiswa) #True -> "True" (string) 
print(nama)

