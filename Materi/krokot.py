def jumlah_krokot():   
    jumlah_benih = int(input("Jumlah Benih Krokot : "))
    jumlah_krokot = int(jumlah_benih * 10) /1000
    kemasan = 1000
    bubuk_per_kg = float(jumlah_krokot / 10)
    bubuk_per_pack = int(bubuk_per_kg / 0.25)
    total_kemasan = int(kemasan * bubuk_per_pack)
    harga_jual_per_250gram = 35000
    total_harga_modal = int(jumlah_benih/200) * 10000
    if jumlah_benih >= 10000:
        pupuk = 300000
        media_tanam = 200000
        tenaga_kerja = 900000
        biaya_operasional = 1000000
        total_harga_modal = int(jumlah_benih/200) * 10000 + pupuk + media_tanam + tenaga_kerja + biaya_operasional
        
        
    total_harga_jual = harga_jual_per_250gram * bubuk_per_pack
    laba_bersih = total_harga_jual - (total_harga_modal + total_kemasan)
    roi = float((total_harga_jual-total_harga_modal)/total_harga_modal) *100
    
    print(f"Jumlah Krokot : {jumlah_krokot:} Kg")
    print(f"Harga Kemasan : Rp {kemasan:,}")
    print(f"Total harga kemasan : Rp {total_kemasan:,}")
    print(f"Modal Bubuk Per {jumlah_krokot} Kg : {bubuk_per_kg:,} Kg")
    print(f"Hasil dari {bubuk_per_kg}  kg :  {bubuk_per_pack} pack")
    print(f"Harga Jual per Pack : Rp {harga_jual_per_250gram:,}")
    print(f"Pupuk dan media tanam : Rp {pupuk + media_tanam:,}")
    print(f"Total Modal Krokot : {total_harga_modal + total_kemasan:,}")
    print(f"Pendapatan  : Rp {total_harga_jual:,}")
    print(f"Laba Bersih : Rp {laba_bersih:,}")
    print(f"ROI : {roi:.2f}%")

# jumlah_krokot()
print("\n\n")

def modal_krokot():
    total_harga_modal = int(input("Total Harga Modal (Rp): "))
    krokot_per_kg = 25000  # Harga per kg krokot segar
    harga_jual_per_250gram = 31000  # Harga jual bubuk krokot per 250 gram
    
    # Menghitung jumlah krokot segar yang dapat dibeli
    jumlah_krokot = total_harga_modal / krokot_per_kg  # dalam kg
    
    # Menghitung hasil bubuk krokot setelah proses pengeringan (setengah dari berat krokot segar)
    bubuk_per_kg = jumlah_krokot / 8  # Hasil bubuk krokot dalam kg
    
    # Menghitung jumlah pack bubuk krokot (1 pack = 250 gram = 0.25 kg)
    bubuk_per_pack = int(bubuk_per_kg / 0.25)  # Jumlah pack 250 gram
    
    # Menghitung total pendapatan dari penjualan
    total_harga_jual = bubuk_per_pack * harga_jual_per_250gram
    
    # Menghitung laba bersih
    laba_bersih = total_harga_jual - total_harga_modal
    
    # Output hasil perhitungan
    print(f"Modal krokot Per 1 Kg : Rp {krokot_per_kg:,}")
    print(f"Total Modal: Rp {total_harga_modal:,}")
    print(f"Jumlah Krokot yang Dibeli: {jumlah_krokot:.2f} Kg")
    print(f"Hasil Bubuk Krokot: {bubuk_per_kg:.2f} Kg")
    print(f"Jumlah Pack 250 gram: {bubuk_per_pack} pack")
    print(f"Harga Jual per Pack: Rp {harga_jual_per_250gram:,}")
    print(f"Pendapatan : Rp {total_harga_jual:,}")
    print(f"Laba Bersih: Rp {laba_bersih:,}")

# modal_krokot()

def hitung_dari_pack():
    jumlah_pack = int(input("Jumlah Pack (250 gram) : "))

    # Konstanta harga dan perhitungan dasar
    berat_per_pack = 0.25  # Berat per pack dalam kg
    krokot_per_kg = 10     # Jumlah krokot segar untuk menghasilkan 1 kg bubuk
    kemasan = 1000         # Harga kemasan per pack dalam Rupiah
    harga_jual_per_pack = 35000

    # Menghitung kebutuhan bahan dan modal
    total_bubuk = jumlah_pack * berat_per_pack
    total_krokot = total_bubuk * krokot_per_kg
    jumlah_benih = total_krokot * 1000 / 10

    # Menghitung harga modal
    harga_benih = (jumlah_benih / 200) * 10000

    if jumlah_benih >= 10000:
        pupuk = 300000
        media_tanam = 200000
        tenaga_kerja = 900000
        # biaya_operasional = 1000000
    else:
        pupuk = 0
        media_tanam = 0

    total_harga_modal = harga_benih + pupuk + media_tanam + tenaga_kerja #+ biaya_operasional
    total_harga_kemasan = kemasan * jumlah_pack

    # Menghitung pendapatan dan laba
    total_harga_jual = jumlah_pack * harga_jual_per_pack
    laba_bersih = total_harga_jual - (total_harga_modal + total_harga_kemasan)
    roi = float((total_harga_jual-total_harga_modal)/total_harga_modal) *100
    
    # Output hasil perhitungan
    print(f"Jumlah Pack : {jumlah_pack} pack")
    print(f"Total Bubuk yang Diperlukan : {total_bubuk:.2f} Kg")
    print(f"Jumlah Krokot Segar yang Diperlukan : {total_krokot:.2f} Kg")
    print(f"Jumlah Benih yang Diperlukan : {jumlah_benih:.0f} benih")
    print(f"Harga Kemasan per Pack : Rp {kemasan:,}")
    print(f"Total Harga Kemasan : Rp {total_harga_kemasan:,}")
    print(f"Harga Jual per Pack : Rp {harga_jual_per_pack:,}")
    print(f"Pupuk dan Media Tanam : Rp {pupuk + media_tanam:,}")
    print(f"Total Modal : Rp {total_harga_modal + total_harga_kemasan:,}")
    print(f"Pendapatan : Rp {total_harga_jual:,}")
    print(f"Laba Bersih : Rp {laba_bersih:,}")
    print(f"ROI : {roi:.2f}%")

hitung_dari_pack()


