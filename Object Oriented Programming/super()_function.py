class bangun_datar:
    def __init__(self, nama,warna, terisi):
        self.nama = nama
        self.warna = warna
        self.terisi = terisi

    def info(self):
        print('Nama:', self.nama)
        print('Warna:', self.warna)
        if self.terisi == True:
            print('Terisi: Ya')
        else:
            print('Terisi: Tidak')
        
        
        

    def hitung_luas(self):
        pass

    def hitung_keliling(self):
        pass
    
class persegi(bangun_datar):
    def __init__(self, nama,warna,terisi, sisi):
        super().__init__(nama,warna, terisi)
        self.sisi = sisi
    
    def hitung_luas(self):
        return self.sisi * self.sisi
        
class lingkaran(bangun_datar):
    def __init__(self, nama,warna,terisi, jari_jari):
        super().__init__(nama,warna, terisi)
        self.jari_jari = jari_jari
        
    def hitung_luas(self):
        return 3.14 * self.jari_jari * self.jari_jari

class segitiga(bangun_datar):
    def __init__(self, nama,warna,terisi, alas, tinggi):
        super().__init__(nama,warna, terisi)
        self.alas = alas
        self.tinggi = tinggi
        
    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

class trapesium(bangun_datar):
    def __init__(self, nama,warna,terisi, sisi1, sisi2, tinggi):
        super().__init__(nama,warna, terisi)
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return 0.5 * (self.sisi1 + self.sisi2) * self.tinggi
    
class jajar_genjang(bangun_datar):
    def __init__(self, nama,warna,terisi, alas, tinggi):
        super().__init__(nama,warna, terisi)
        self.alas = alas
        self.tinggi = tinggi
        
    def hitung_luas(self):
        return self.alas * self.tinggi
        
class layang_layang(bangun_datar):
    def __init__(self,nama,warna,terisi, diagonal1, diagonal2, sisi1, sisi2):
        super().__init__(nama,warna, terisi)
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        
    def hitung_luas(self):
        return 0.5 * self.diagonal1 * self.diagonal2
        
class belah_ketupat(bangun_datar):
    def __init__(self, nama, diagonal1, diagonal2, sisi):
        super().__init__(nama)
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.sisi = sisi
    
    def hitung_luas(self):
        return 0.5 * self.diagonal1 * self.diagonal2
        
class persegi_panjang(bangun_datar):
    def __init__(self, nama,warna, terisi, panjang, lebar):
        super().__init__(nama,warna, terisi)
        self.panjang = panjang
        self.lebar = lebar
    
    def hitung_luas(self):
        return self.panjang * self.lebar
        
Persegi = persegi('Persegi', 'Merah', True, 4)
Persegi.info()
print(Persegi.sisi) 

print()

Lingkaran = lingkaran('Lingkaran', 'Biru', False , 7)
print(Lingkaran.info())
print(Lingkaran.jari_jari)

Persegi_panjang = persegi_panjang('Persegi Panjang', 'Hijau', True, 5, 3)
print(Persegi_panjang.info())
print(f"Luas Persegi Panjang : {Persegi_panjang.hitung_luas()}")