class keluarga:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampilkan(self):
        print("Nama: ", self.nama)
        print("Umur: ", self.umur)
        
class ayah(keluarga):
    pass

class ibu(keluarga):
    pass
    
class anak(keluarga):
    pass

Ayah = ayah('Budi', 47)
Ibu = ibu('Yustina', 48)
Anak = anak('Surya', 20)

for obj in [Ayah, Ibu, Anak]:
    obj.tampilkan()
    print()
