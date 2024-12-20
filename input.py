
def biodata() :
    nama= input('Masukkan nama anda: ') #inputan default adalah string
    age= int(input('Masukkan umur anda: ')) #inputan akan diubah menjadi integer
    age= age+ 5    #menambahkan 5 tahun dari umur yang diinputkan

    print(f"Namaku adalah {nama}")
    print(f"5 Tahun dari umur saya adalah {age}")
    
#biodata() #memanggil fungsi biodata()

def luasPersegiPanjang() :
    panjang= int(input('Masukkan panjang: ')) #inputan akan diubah menjadi integer
    lebar= int(input('Masukkan lebar: ')) #inputan akan diubah menjadi integer
    luas= panjang*lebar
    print(f"Luas persegi panjang adalah {luas} cm")

#luasPersegiPanjang() #memanggil fungsi luasPersegiPanjang()

def matriks() :
    #membuat matriks 2x2
    matriks= [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            matriks[i][j]= int(input(f"Masukkan nilai matriks baris ke-{i+1} kolom ke-{j+1}: ")) #inputan akan diubah menjadi integer
    print(f"Matriks yang anda masukkan adalah: {matriks}")
    
#matriks() #memanggil fungsi matriks()

def restorant():
    makanan= input('Masukkan nama makanan: ')
    harga_makanan= int(input('Masukkan harga makanan: '))
    jumlah_makanan= int(input('Masukkan jumlah makanan: '))
    minuman= input('Masukkan nama minuman: ') 
    harga_minuman= int(input('Masukkan harga minuman: ')) 
    jumlah_minuman= int(input('Masukkan jumlah minuman: '))
    
    total_harga= (harga_makanan*jumlah_makanan)+(harga_minuman*jumlah_minuman) #menghitung total harga
    print(f"Total harga yang harus anda bayar adalah: Rp {total_harga:,.0f}") #format rupiah
    
#restorant() #memanggil fungsi beli_barang()

