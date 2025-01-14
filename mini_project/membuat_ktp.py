def biodata(nik, nama, tanggal_lahir, jenis_kelamin, alamat, agama, status_kawin, pekerjaan, kewarganegaraan, berlaku):
    field_width = 35
    print ("┌──────────────────────────────────────────────────────────┐")
    print ("│                  PROVINSI JAWA SELATAN                   │")
    print ("│                  KABUPATEN GEDANG IJO                    │")
    print(f"│  {'NIK':<18}: {nik:<{field_width-14}} ┌──────────┐  │")
    print(f"│  {'Nama':<18}: {nama:<{field_width-14}} │          │  │")
    print(f"│  {'Tanggal Lahir':<18}: {tanggal_lahir:<{field_width-14}} │          │  │")
    print(f"│  {'Jenis Kelamin':<18}: {jenis_kelamin:<{field_width-14}} │          │  │")
    print(f"│  {'Alamat':<18}: {alamat:<{field_width-14}} │          │  │")
    print(f"│  {'Agama':<18}: {agama:<{field_width-14}} │          │  │")
    print(f"│  {'Status Perkawinan':<18}: {status_kawin:<{field_width-14}} │          │  │")
    print(f"│  {'Pekerjaan':<18}: {pekerjaan:<{field_width-14}} └──────────┘  │")
    print(f"│  {'Kewarganegaraan':<18}: {kewarganegaraan:<{field_width}} │")
    print(f"│  {'Berlaku':<18}: {berlaku:<{field_width}} │")
    print ("└──────────────────────────────────────────────────────────┘")

print("┌─────────────────────┐")
print("│  Selamat datang di  │")
print("│  Pembuatan KTP KW!  │")
print("└─────────────────────┘")
biodata(1010101010101010, "SURYA DWI SATRIA", "01-01-2001", "LAKI-LAKI", "KONOHA", "ISLAM", "BELUM KAWIN", "BILIONARE", "WNI", "SEUMUR HIDUP")
print("Ini adalah contoh biodata yang akan dibuat")
pilih=int(input("Apakah kamu ingin membuat biodata? (1) Ya (2) Tidak: "))

while True:
    if pilih==1:
        print("┌─────────────────────┐")
        print("│   Silahkan mengisi  │")
        print("│    Informasi dulu!  │")
        print("└─────────────────────┘")
        nik = input("NIK" + " " * (18 - len("NIK")) + ": ")
        nama = input("Nama" + " " * (18 - len("Nama")) + ": ")
        tanggal_lahir = input("Tanggal Lahir" + " " * (18 - len("Tanggal Lahir")) + ": ")
        jenis_kelamin = input("Jenis Kelamin" + " " * (18 - len("Jenis Kelamin")) + ": ")
        alamat = input("Alamat" + " " * (18 - len("Alamat")) + ": ")
        agama = input("Agama" + " " * (18 - len("Agama")) + ": ")
        status_kawin = input("Status Perkawinan" + " " * (18 - len("Status Perkawinan")) + ": ")
        pekerjaan = input("Pekerjaan" + " " * (18 - len("Pekerjaan")) + ": ")
        kewarganegaraan = input("Kewarganegaraan" + " " * (18 - len("Kewarganegaraan")) + ": ")
        berlaku = input("Berlaku" + " " * (18 - len("Berlaku")) + ": ")
        biodata(nik, nama, tanggal_lahir, jenis_kelamin, alamat, agama, status_kawin, pekerjaan, kewarganegaraan, berlaku)
        pilihan = int(input("Apakah kamu ingin membuat biodata lagi? (1) Ya (2) Tidak: "))
        print(type(pilihan))
        print(pilihan)
        if pilihan == 1:
            continue
        elif pilihan == 2:
            break
        else:
            print("Pilihan tidak ada")
            # Ask again for the choice
            pilihan = int(input("Apakah kamu ingin membuat biodata lagi? (1) Ya (2) Tidak: "))
        
        

