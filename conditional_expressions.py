def number_check():
    while True:
        try:
            number = int(input("Masukkan angka: "))
            print("Angka positif" if number > 0 else "Angka negatif atau nol")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def ganjil_genap():
    while True:
        try:
            number = int(input("Masukkan angka yang diinginkan: "))
            print("Angka Genap" if number % 2 == 0 else "Angka Ganjil")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def angka_prima():
    while True:
        try:
            number = int(input("Masukkan angka yang ingin dicek (atau ketik 'q' untuk keluar): "))
            
            # Angka prima harus lebih dari 1
            is_prime = number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))
            
            result = "Angka Prima" if is_prime else "Bukan Angka Prima"
            print(result)
        
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
        except KeyboardInterrupt:
            print("\nProgram dihentikan. Terima kasih!")
            break

# Uncomment salah satu fungsi untuk dijalankan
# number_check()
# ganjil_genap()
angka_prima()