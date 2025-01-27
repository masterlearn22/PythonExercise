def materi():
    
    # class method adalah method yang dimiliki oleh class itu sendiri dan bukan oleh instance dari class tersebut
    # class method biasanya digunakan untuk mengakses atribut class dan mengubah atribut class
    
    class mahasiswa:
        
        jumlah_mahasiswa = 0
        rata_rata_ipk = 0
        
        def __init__(self, nama, nim,ipk):
            self.nama = nama
            self.nim = nim
            self.ipk = ipk
            mahasiswa.jumlah_mahasiswa += 1
            mahasiswa.rata_rata_ipk += ipk
        
        def info(self):
            print(f"Nama: {self.nama}\nNIM: {self.nim}\nIPK: {self.ipk}")
            
        @classmethod
        def jumlah(cls):
            return cls.jumlah_mahasiswa
        
        @classmethod
        def rata(cls):
            if cls.jumlah_mahasiswa == 0:
                return 0
            return cls.rata_rata_ipk / cls.jumlah_mahasiswa
        
    
    mhs1 = mahasiswa("Surya", "123", 3.5)
    mhs2 = mahasiswa("Budi", "124", 3.2)
    mhs3 = mahasiswa("Andi", "125", 3.7)
    mhs4 = mahasiswa("Dedi", "126", 3.2)
    mhs5 = mahasiswa("Rahmad", "127", 3.9)
    
    for mhs in (mhs1, mhs2, mhs3, mhs4, mhs5):
        mhs.info()
        print()
    print(f"Jumlah Mahasiswa: {mahasiswa.jumlah()}")
    print(f"Rata-rata IPK: {mahasiswa.rata():.2f}")
    
# materi()

def exercise():
    class Perabotan:
        jumlah_perabotan = 0
        nama_perabotan = []
        harga_total = 0
        uang = 1000000

        def __init__(self, nama, harga):
            self.nama = nama
            self.harga = harga
            Perabotan.jumlah_perabotan += 1
            Perabotan.harga_total += harga

        def info(self): 
            print(f"Nama: {self.nama}\nHarga: {self.harga}")

        @classmethod
        def total(cls):
            return cls.harga_total

        @classmethod
        def jumlah(cls):
            return cls.jumlah_perabotan

        @classmethod
        def beli(cls):
            if cls.harga_total <= cls.uang:
                cls.nama_perabotan = [barang1.nama, barang2.nama, barang3.nama]
                print(f"Perabotan {', '.join(cls.nama_perabotan)} berhasil dibeli!")
                cls.uang -= cls.harga_total
                print(f"Uang tersisa: Rp {cls.uang:,}")
            else:
                print(f"Uang tidak cukup untuk membeli semua perabotan. Total harga: Rp {cls.harga_total:,}, Uang tersedia: Rp {cls.uang:,}")

    # Membuat instance perabotan
    barang1 = Perabotan("Meja", 400000)
    barang2 = Perabotan("Kursi", 300000)
    barang3 = Perabotan("Lemari", 200000)

    # Menampilkan informasi setiap barang
    for barang in (barang1, barang2, barang3):
        barang.info()
        print()

    # Menampilkan informasi total
    print(f"Jumlah Uang: Rp {Perabotan.uang:,}")
    print(f"Jumlah Perabotan: {Perabotan.jumlah()}")
    print(f"Total Harga: Rp {Perabotan.total():,}\n")

    # Memproses pembelian
    Perabotan.beli()

# Memanggil fungsi exercise
exercise()


        
            