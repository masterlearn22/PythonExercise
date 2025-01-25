import datetime

# tanggal_input = input("Masukkan tanggal (DD-MM-YYYY): ")
tanggal_input = "22-12-2004"
tanggal_parts = tanggal_input.split("-")
tanggal = datetime.date(int(tanggal_parts[2]), int(tanggal_parts[1]), int(tanggal_parts[0]))
hari_ini = datetime.date.today()
print(tanggal)
print(hari_ini)

waktu = datetime.time(11,45,0)
waktu_saat_ini = datetime.datetime.now()
print(waktu)
print(waktu_saat_ini)

now = datetime.datetime.now()
sekarang = now.strftime("%H:%M:%S , %d-%m-%Y")
print(sekarang)

deadline = datetime.datetime(2020,12,31, 23,59,59)
current_datetime = datetime.datetime.now()

if deadline > current_datetime:
    print("Waktu masih ada")
else:
    print("Waktu sudah habis")