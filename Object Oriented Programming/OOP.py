class mobil:
    def __init__(self,model,tahun,warna, plat):
        self.model = model
        self.tahun = tahun
        self.warna = warna
        self.plat = plat
    
    def jalan(self):
        print('Mobil', self.model, 'Jalan')
        
    def rem(self):
        print('Mobil', self.model, 'Berhenti')

    def info(self):
        print('Model:', self.model)
        print('Tahun:', self.tahun)
        print('Warna:', self.warna)
        print('Plat:', self.plat)
        
mobil1 = mobil('Toyota Avanza', 2019, 'Hitam', 'B 1234 ABC') #mobil1 adalah object dari class mobil
mobil1.jalan() # mengakses method jalan dari object mobil1
mobil1.rem() # mengakses method rem dari object mobil1
mobil1.info() # mengakses method info dari object mobil1

print()

mobil2 = mobil('Honda Jazz', 2018, 'Putih', 'B 5678 DEF')
mobil2.jalan()
mobil2.rem()
mobil2.info()

print()

mobil3 = mobil('Suzuki Ertiga', 2017, 'Merah', 'B 9101 GHI')
mobil3.jalan()
mobil3.rem()
mobil3.info()

print()

mobil4 = mobil('Mitsubishi Xpander', 2016, 'Biru', 'B 1121 JKL')
mobil4.jalan()
mobil4.rem()
mobil4.info()
