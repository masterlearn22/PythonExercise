def biodata() : 
    nama = input("Masukkan nama: ")

    while nama == None or nama == "":
        print("Nama tidak boleh kosong")
        nama = input("Masukkan nama: ")

    umur = int(input("Masukkan umur: "))
    while umur < 17:
        print("Umur harus lebih dari 17 tahun")
        umur = int(input("Masukkan umur: "))
        
    print(f"Nama: {nama}")
    print(f"Umur: {umur}")

def test_str():
    buah = []
    while True:
        buahan= input("Masukkan nama buah: ")
        if buahan == "q":
            break
        buah.append(buahan)

    print(f"Buah yang anda masukkan adalah: {buah}")
test_str()