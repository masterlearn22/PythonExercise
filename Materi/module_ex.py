import random

def calculator():
    print("Kalkulator Sederhana")
    print("Masukkan '=' untuk menghentikan kalkulator.")
    
    result = 0
    operator = None

    while True:
        if operator is None:
            num1 = float(input("Masukkan angka: "))
        else:
            num1 = result  # Gunakan hasil sebelumnya sebagai angka

        operator = input("Operator (+, -, *, /): ")

        if operator == '=':
            print(f"Hasil akhir: {result}")
            break

        num2 = float(input("Masukkan angka: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
                continue
        else:
            print("Operator tidak valid. Silakan coba lagi.")
            continue

        print(f"Hasil: {result}")

def dua_dadu():
    print("┌─────────────────────┐")
    print("│  Selamat datang di  │")
    print("│    Permainan Dadu!  │")
    print("└─────────────────────┘")
    dice ={
    1: ("┌─────────┐\n"
        "│         │\n"
        "│    ●    │\n"
        "│         │\n"
        "└─────────┘"),
    2: ("┌─────────┐\n"
        "│  ●      │\n"
        "│         │\n"
        "│      ●  │\n"
        "└─────────┘"),
    3: ("┌─────────┐\n"
        "│ ●       │\n"
        "│    ●    │\n"
        "│       ● │\n"
        "└─────────┘"),
    4: ("┌─────────┐\n"
        "│  ●   ●  │\n"
        "│         │\n"
        "│  ●   ●  │\n"
        "└─────────┘"),
    5: ("┌─────────┐\n"
        "│  ●   ●  │\n"
        "│    ●    │\n"
        "│  ●   ●  │\n"
        "└─────────┘"),
    6: ("┌─────────┐\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "└─────────┘"),
}
    number_dic1 = random.randint(1, 6)
    number_dic2 = random.randint(1, 6)

    # Print the results
    print(f"Hasil dadu: {number_dic1} dan {number_dic2}")

    # Print the two dice side by side
    dice1 = dice[number_dic1].splitlines()
    dice2 = dice[number_dic2].splitlines()

    for line1, line2 in zip(dice1, dice2):
        print(line1 + "  " + line2)   
    
def pemesanan_menu():
    makanan ={
        "Pecel" : 8000,
        "Nasi goreng" : 10000,
        "Rujak" : 7000,
        "Soto": 15000,
        "Rawon": 12000,
    }

    minuman = {
        "Jus buah" : 5000,
        "Kopi" : 3000,
        "Teh" : 2000, 
        "Smothie" :12000
    }

    cart=[]
    total=0
    print("------Daftar makanan------")
    for key, values in makanan.items():
        print(f"{key:13} : Rp {values:,}")
    print("--------------------------")
    
    print("\n------Daftar Minuman------")  
    for key, values in minuman.items():
        print(f"{key:13} : Rp {values:,}")
    print("--------------------------")

    while True:
        while True:
            
            pilih_makanan = input("Masukkan makanan yang ingin dibeli (atau 'q' untuk selesai): ").capitalize()
            if pilih_makanan == 'Q':
                break
            if makanan.get(pilih_makanan): #cara 1
                cart.append(pilih_makanan)
                total += makanan[pilih_makanan]
            else:
                print("Makanan tidak tersedia.")
            
        while True:
            pilih_minuman = input("Masukkan minuman yang ingin dibeli (atau 'q' untuk selesai): ").capitalize()
            if pilih_minuman == 'Q':
                break
            if pilih_minuman in minuman: #cara 2
                cart.append(pilih_minuman)
                total += minuman[pilih_minuman]
            else:
                print("Minuman tidak tersedia.")
        break
        
    print("\n---------Pesanan---------")
    for item in cart:
        if item in makanan:
            print(f"{item:13} : Rp {makanan[item]:,}")
        elif item in minuman:
            print(f"{item:13} : Rp {minuman[item]:,}")
    print("-------------------------")

    print(f"{'Total':13} : Rp {total:,}")

def tebak_tangan():
    lawan ={1:"kertas", 2:"batu", 3:"gunting"}
    kawan ={1:"kertas", 2:"batu", 3:"gunting"}
    while True:
        saya =int(input("ajukan : "))
        random_lawan = random.randint(1, 3)
        print(f"Lawan memilih: {lawan[random_lawan]}")
        if saya == random_lawan:
            print("Seri!")
            break
        elif (saya == 1 and random_lawan == 2) or (saya == 2 and random_lawan == 3) or (saya == 3 and random_lawan == 1):
            print(f"Menang!kamu memilih {kawan[saya]}")
            break
        else:
            print(f"Kalah!kamu memilih {kawan[saya]}")
            break
        print(random_lawan)

