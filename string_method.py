def mencari_huruf() :  
    while True :
        nama = input("Masukkan nama Anda: ")
        result = int(nama.find(input("Masukkan huruf yang ingin dicari: "))) +1 # find() mencari huruf yang diinputkan pada variabel "nama"
        print(result)
        
def mengukur_kata():
    while True:
        kalimat = input("Masukkan kalimat yang ingin diukur: ")
        spasi = int(kalimat.count(" ")) # mencari dan menhitung jumlah spasi dari variabel ""kalimat"
        result = len(kalimat) - spasi
        print(result)
        
print("Selamat mencoba berbagai macam string method!")
print("Pilihlah menu yang ingin Anda lakukan:")
print("1. Mencari huruf")
print("2. Mengukur kata")
pilihan = int(input("Masukkan pilihan Anda: "))
if pilihan == 1:
    mencari_huruf()
elif pilihan == 2:
    mengukur_kata()
else:
    print("Pilihan tidak tersedia")