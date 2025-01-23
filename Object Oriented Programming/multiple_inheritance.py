class universitas:
    def __init__(self, nama_universitas, alamat_universitas):
        self.nama_universitas = nama_universitas
        self.alamat_universitas = alamat_universitas
    
    def info_univ(self):
        print('Nama Universitas:', self.nama_universitas)
        print('Alamat Universitas:', self.alamat_universitas)
        
class fakultas(universitas):
    def __init__(self, nama_universitas, alamat_universitas, nama_fakultas):
        super().__init__(nama_universitas, alamat_universitas)
        self.nama_fakultas = nama_fakultas
        
    def info_fakultas(self):
        print('Nama Fakultas:', self.nama_fakultas)
        

        
class jurusan(fakultas):
    def __init__(self, nama_universitas, alamat_universitas, nama_fakultas, nama_jurusan):
        super().__init__(nama_universitas, alamat_universitas, nama_fakultas)
        self.nama_jurusan = nama_jurusan
    
    def info_jurusan(self):
        print('Nama Jurusan:', self.nama_jurusan)
        
#Role Class
class mahasiswa(jurusan):
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        
    def info_mhs(self):
        print('Nama:', self.nama)
        print('NIM:', self.nim)
        print('Jurusan:', self.jurusan)
    

# Membuat objek dari kelas mahasiswa
class dosen(jurusan):
    def __init__(self, nama, nip, jurusan):
        self.nama = nama
        self.nip = nip
        self.jurusan = jurusan
    
    def info_dosen(self):
        print('Nama:', self.nama)
        print('NIP:', self.nip)
        print('Jurusan:', self.jurusan)
        
   
        
class pengajar(dosen):
    def penelitian(self):
        print('Dosen', self.nama, 'melakukan penelitian')
        
    def mendapat_gaji(self):
        print('Dosen', self.nama, 'mendapat gaji')
        
    def mengajar(self):
        print('Dosen', self.nama, 'mengajar')

class pembelajar(mahasiswa):
    def research(self):
        print('Mahasiswa', self.nama, 'melakukan penelitian')
        
    def mendapat_beasiswa(self):
        print('Mahasiswa', self.nama, 'mendapat beasiswa')
    
    def belajar(self):
        print('Mahasiswa', self.nama, 'belajar keras')

# Membuat objek dari kelas jurusan
jurusan1 = jurusan('Universitas Gadjah Mada', 'Yogyakarta', 'Fakultas Teknik', 'Teknik Informatika')
jurusan1.info_univ()  # Info universitas
jurusan1.info_fakultas()  # Info fakultas
jurusan1.info_jurusan()  # Info jurusan

mahasiswa1 = pembelajar('Budi', '123456', 'Teknik Informatika')
mahasiswa1.belajar()

dosen1 = pengajar('Susi', '123456', 'Teknik Informatika')
dosen1.mengajar()
