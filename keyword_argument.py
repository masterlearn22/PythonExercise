def ucapan(pembuka, isi, penutup,nama):
    print(f"Halo {nama},")
    print(pembuka)
    print(isi)
    print(penutup)
    
ucapan("Selamat datang dipembukaan Rumah Makan Padang",nama="Surya Dwi Satria",isi="Di sini kita akan berdiskusi tentang bagaimana program penjualan rumah makan akan dijalankan",penutup="Terima Kasih")
#Denagan menggunakan Keyword Argumen kita dapat memanggil function dengan values yang tidak urut, namun values pertama harus didepan

def nomor_hp(negara,area,awal, akhir):
    if negara == 62:
        print("Indonesia")
    negara = 0
    return f"{negara}{area}-{awal}-{akhir}"
     
phone_num = nomor_hp(negara=62,area=857,awal=3003,akhir=3426)
print(phone_num)