def jumlah_krokot():
    try:
        jumlah_benih = int(input("Jumlah Benih Krokot: "))
        jumlah_krokot = int(jumlah_benih * 10) / 1000  # Hasil krokot segar dalam kg
        kemasan = 1000  # Harga kemasan per pack dalam Rupiah
        bubuk_per_kg = jumlah_krokot / 10  # Hasil bubuk krokot setelah proses pengeringan
        bubuk_per_pack = int(bubuk_per_kg / 0.25)  # Jumlah pack 250 gram
        total_kemasan = kemasan * bubuk_per_pack  # Total biaya kemasan
        harga_jual_per_250gram = 35000  # Harga jual per pack (250 gram)
        total_harga_modal = (jumlah_benih / 200) * 10000  # Harga modal berdasarkan benih

        # Biaya tambahan jika benih >= 10.000
        if jumlah_benih >= 10000:
            pupuk = 300000
            media_tanam = 200000
            tenaga_kerja = 900000
            biaya_operasional = 1000000
            total_harga_modal += pupuk + media_tanam + tenaga_kerja + biaya_operasional
        else:
            pupuk = 0
            media_tanam = 0
            tenaga_kerja = 0

        total_harga_jual = harga_jual_per_250gram * bubuk_per_pack
        laba_bersih = total_harga_jual - (total_harga_modal + total_kemasan)
        roi = (laba_bersih / total_harga_modal) * 100

        # Output hasil
        print("\nHasil Perhitungan:")
        print(f"Jumlah Krokot Segar: {jumlah_krokot:.2f} Kg")
        print(f"Hasil Bubuk Krokot: {bubuk_per_kg:.2f} Kg")
        print(f"Jumlah Pack (250 gram): {bubuk_per_pack} pack")
        print(f"Harga Kemasan per Pack: Rp {kemasan:,}")
        print(f"Total Harga Kemasan: Rp {total_kemasan:,}")
        print(f"Total Modal: Rp {total_harga_modal + total_kemasan:,}")
        print(f"Pendapatan: Rp {total_harga_jual:,}")
        print(f"Laba Bersih: Rp {laba_bersih:,}")
        print(f"ROI: {roi:.2f}%")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

def modal_krokot():
    try:
        total_harga_modal = int(input("Total Harga Modal (Rp): "))
        krokot_per_kg = 25000  # Harga per kg krokot segar
        harga_jual_per_250gram = 31000  # Harga jual bubuk krokot per 250 gram

        jumlah_krokot = total_harga_modal / krokot_per_kg  # Krokot segar dalam kg
        bubuk_per_kg = jumlah_krokot / 8  # Bubuk krokot dalam kg
        bubuk_per_pack = int(bubuk_per_kg / 0.25)  # Jumlah pack 250 gram
        total_harga_jual = bubuk_per_pack * harga_jual_per_250gram  # Total pendapatan
        laba_bersih = total_harga_jual - total_harga_modal  # Laba bersih

        # Output hasil
        print("\nHasil Perhitungan:")
        print(f"Modal Krokot per 1 Kg: Rp {krokot_per_kg:,}")
        print(f"Total Modal: Rp {total_harga_modal:,}")
        print(f"Jumlah Krokot Segar: {jumlah_krokot:.2f} Kg")
        print(f"Hasil Bubuk Krokot: {bubuk_per_kg:.2f} Kg")
        print(f"Jumlah Pack (250 gram): {bubuk_per_pack} pack")
        print(f"Harga Jual per Pack: Rp {harga_jual_per_250gram:,}")
        print(f"Pendapatan: Rp {total_harga_jual:,}")
        print(f"Laba Bersih: Rp {laba_bersih:,}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

def hitung_dari_pack():
    try:
        jumlah_pack = int(input("Jumlah Pack (250 gram): "))

        berat_per_pack = 0.25  # Berat per pack dalam kg
        krokot_per_kg = 10  # Krokot segar untuk menghasilkan 1 kg bubuk
        kemasan = 1000  # Harga kemasan per pack
        harga_jual_per_pack = 35000  # Harga jual per pack

        total_bubuk = jumlah_pack * berat_per_pack
        total_krokot = total_bubuk * krokot_per_kg
        jumlah_benih = total_krokot * 1000 / 10

        harga_benih = (jumlah_benih / 200) * 10000
        if jumlah_benih >= 10000:
            pupuk = 300000
            media_tanam = 200000
            tenaga_kerja = 900000
        else:
            pupuk = 0
            media_tanam = 0
            tenaga_kerja = 0

        total_harga_modal = harga_benih + pupuk + media_tanam + tenaga_kerja
        total_harga_kemasan = kemasan * jumlah_pack
        total_harga_jual = jumlah_pack * harga_jual_per_pack
        laba_bersih = total_harga_jual - (total_harga_modal + total_harga_kemasan)
        roi = (laba_bersih / total_harga_modal) * 100

        # Output hasil
        print("\nHasil Perhitungan:")
        print(f"Jumlah Pack: {jumlah_pack} pack")
        print(f"Total Bubuk Krokot: {total_bubuk:.2f} Kg")
        print(f"Jumlah Krokot Segar: {total_krokot:.2f} Kg")
        print(f"Jumlah Benih: {jumlah_benih:.0f} benih")
        print(f"Total Modal: Rp {total_harga_modal + total_harga_kemasan:,}")
        print(f"Pendapatan: Rp {total_harga_jual:,}")
        print(f"Laba Bersih: Rp {laba_bersih:,}")
        print(f"ROI: {roi:.2f}%")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")
