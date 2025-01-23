def string():    
    brand= "XIAOMI"
    while True:
        tebak=input("tebak huruf yang ada di nama Brand ini! \n")
        if tebak.upper() == brand:
            print(f"Benar ! jawabanya adalah Brand {brand}")
            break
        elif tebak.upper() in brand:
            print(f"Benar ! huruf {tebak} ada di nama Brand")
        else:
            print(f"Salah ! huruf {tebak} tidak ada di nama Brand")
# string()        
        
def list():        
    buahan = ["apel","pisang","anggur","durian","semangka"]
    while True: 
        tebak=input("tebak buah yang ada di list ini! \n")
        if tebak in buahan:
            print(f"Benar ! buah {tebak} ada di list")
            break
        else:
            print(f"Salah ! buah {tebak} tidak ada di list")
# list()

def dictionary():
    values = {
        "A": 4,
        "AB": 3.5,
        "B": 3,
        "BC": 2.5,
        "C": 2,
        "D": 1,
        "E": 0
    }

    print("Nilai yang tersedia:", end=" ")
    for key in values:
        print(key, end=" ")
    print()

    while True:
        value = input("Ingin lihat nilai apa? (masukkan nilai atau huruf)\n").strip().upper()
        #strip() untuk menghapus karakter whitespace(spasi, tab, newline, dll.)
        
        # cek apakah input ada di dalam values
        if value in values:
            print(f"Nilai {value} adalah {float(values[value])}")

        # cek apakah input dalam bentuk angka atau float, tidak peduli walaupun input tersebut adalah string
        # yang penting hanya dalam bentuk angka, jika float maka akan di ubah dalam bentuk angka
        # jika  float 2.5 di ubah dalam bentuk 25 menghilangkan . menjadi ''
        elif value.isdigit() or (value.replace('.', '', 1).isdigit() and value.count('.') < 2):  
            numeric_value = float(value) #mengubah input menjadi float
            # Find the corresponding key for the numeric value
            for key, val in values.items():
                if val == numeric_value:
                    print(f"Nilai {numeric_value} adalah {key}")
                    break
            else:
                print("Nilai tidak ditemukan. Silakan masukkan nilai yang valid.")
        else:
            print("Nilai tidak ditemukan. Silakan masukkan nilai yang valid.") 
dictionary()
    
