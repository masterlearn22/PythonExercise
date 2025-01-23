def tambah(*hitung): # dengan arg bisa menerima berapapun argumen
    total = 0
    for angka in hitung:
        total += angka
    print (total)

tambah(10,1,5)

def nama_lengkap(*nama):
    for nama in nama:
        print(nama,end=" ")
        
nama_lengkap("Surya","Dwi","Satria")

print()

def alamat(**domisili): #KWARG
    for key,values in domisili.items(): #CARA 1
        print(f"{key:8} : {values}")
    print()
    for key in domisili.keys():
        print(f"{key:8} : {domisili[key]}") #CARA 2
    print()
    for value in domisili.values():
        print(f"{value}")

alamat(
    lokasi="Jakarta",
    alamat="Jl. Kuningan",
    kodepos="12710",
    negara="Indonesia",
)
print()
def belanja(*arg,**kwarg): #ARG & KWARG
    print(f"Hello {arg[0]}\nNIM kamu adalah {arg[1]} dan kamu belanja di {kwarg.get('alamat')} dan \nberasal dari negara {kwarg.get('negara')} ")
    for key,values in kwarg.items():
        print(f"{key} : {values}")

belanja("Surya","434231048",
        alamat= "Surabaya",
        kodepos="12345",
        negara="Indonesia",
        )

