import module_ex

#print(help('modules')) #module yang dapat digunakan di python
while True:
    print("┌─────────────────────┐")
    print("│  Selamat datang di  │")
    print("│   Random Program    │")
    print("└─────────────────────┘")

    pilih = input("Pilih program yang ingin kamu jalankan: ")
    if pilih == "1":
        print("-------Menjalankan Program calculator-------")
        module_ex.calculator()
    elif pilih == "2":
        print("-------Menjalankan Program dua dadu-------")
        module_ex.dua_dadu()
    elif pilih == "3":
        print("-------Menjalankan Program pemesanan makanan-------")
        module_ex.pemesanan_menu()
    elif pilih == "4":
        print("-------Menjalankan Program tebak tangan-------")
        module_ex.tebak_tangan()
    else:
        print("-------Program tidak ada-------")
        break
    