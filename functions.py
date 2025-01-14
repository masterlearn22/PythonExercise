def biodata(nik, nama, tanggal_lahir, jenis_kelamin, alamat, agama, status_kawin, pekerjaan, kewarganegaraan, berlaku):
    field_width = 21  # Adjust this width as needed

    print("┌─────────────────────────────────────────┐")
    print("│            PROVINSI JAWA TIMUR          │")
    print("│            KABUPATEN JOMBANG            │")
    print(f"│  {'NIK':<15}: {nik:<{field_width}} │")
    print(f"│  {'Nama':<15}: {nama:<{field_width}} │")
    print(f"│  {'Tanggal Lahir':<15}: {tanggal_lahir:<{field_width}} │")
    print(f"│  {'Jenis Kelamin':<15}: {jenis_kelamin:<{field_width}} │")
    print(f"│  {'Alamat':<15}: {alamat:<{field_width}} │")
    print(f"│  {'Agama':<15}: {agama:<{field_width}} │")
    print(f"│  {'Status Kawin':<15}: {status_kawin:<{field_width}} │")
    print(f"│  {'Pekerjaan':<15}: {pekerjaan:<{field_width}} │")
    print(f"│  {'Kewarganegaraan':<15}: {kewarganegaraan:<{field_width}} │")
    print(f"│  {'Berlaku':<15}: {berlaku:<{field_width}} │")
    
    # Print the footer
    print("└─────────────────────────────────────────┘")

# CONTOH PANGGILAN
biodata(1010101010101010, "SURYA DWI SATRIA", "01-01-2001", "LAKI-LAKI", "KONOHA", "ISLAM", "BELUM KAWIN", "BILIONARE", "WNI", "SEUMUR HIDUP")