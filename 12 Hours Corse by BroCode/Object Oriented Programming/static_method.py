def materi():
    class karyawan:
        def __init__(self, nama, posisi):
            self.nama = nama
            self.posisi = posisi
        
        def info(self):
            print(f"Nama : {self.nama}")
            print(f"Posisi : {self.posisi}")
            
        @staticmethod
        def is_posisi_tersedia(posisi):
            posisi_tersedia = ['manager', 'QA', 'programmer', 'designer', 'HRD', 'Data Analyst']
            return posisi in posisi_tersedia
                
    #instance method harus membuat instance dari class terlebih dahulu untuk bisa dipanggil           
    karyawan1 = karyawan('Budi', 'manager')
    print(karyawan1.info())
    
    #Static method bisa dipanggil langsung dari class tanpa harus membuat instance dari class tersebut
    print(karyawan1.is_posisi_tersedia('manager')) #True
    print(karyawan.is_posisi_tersedia('Data Scientist')) #False
    print(karyawan.is_posisi_tersedia('Data Analyst')) #True
    
# materi()

def exercise():
    class layanan:
        def __init__(self, nama, harga):
            self.nama = nama
            self.harga = harga
            
        def info(self):
            print(f"Nama : {self.nama}")
            print(f"Harga : {self.harga}")
            
        def diskon(self, persen):
            potongan = self.harga * persen / 100
            self.harga -= potongan
            return potongan
            
        
        @staticmethod
        def validation(saldo, harga):
            if saldo >= harga:
                return True
            else:
                return False
            
        

     # Membuat instance layanan
    layanan1 = layanan('Cuci Motor', 60000)

    # Menampilkan informasi layanan
    layanan1.info()

    # Diskon
    print(f"Potongan harga : {layanan1.diskon(20)}")
    print(f"Harga saat ini : {layanan1.harga}")
    
    saldo = 54000
    
    # Validasi saldo
    if layanan.validation(saldo, layanan1.harga):
        print(f"Saldo {saldo} cukup untuk menggunakan layanan ini.")
    else:
        print(f"Saldo {saldo} tidak cukup untuk menggunakan layanan ini.")
        
    
    

exercise()      

        
    
            