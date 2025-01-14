import random

#● ┌ ─ ┐ │ └ ┘

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

def satu_dadu():
    number_dic=random.randint(1,6)
    print(f"Hasil dadu: {number_dic}")
    print(dice[number_dic])
    return number_dic

def dua_dadu():
    number_dic1 = random.randint(1, 6)
    number_dic2 = random.randint(1, 6)

    # Print the results
    print(f"Hasil dadu: {number_dic1} dan {number_dic2}")

    # Print the two dice side by side
    dice1 = dice[number_dic1].splitlines()
    dice2 = dice[number_dic2].splitlines()

    for line1, line2 in zip(dice1, dice2):
        print(line1 + "  " + line2)
   
#● ┌ ─ ┐ │ └ ┘     
print("┌─────────────────────┐")
print("│  Selamat datang di  │")
print("│    Permainan Dadu!  │")
print("└─────────────────────┘")
while True:
    print("\n1. Main Dadu 1 Buah")
    print("2. Main Dadu 2 Buah")
    pilih =int(input("Pilih dadu yang ingin digunakan : "))
    print("Masukkan '0' jika ingin keluar")
    if pilih == 1:
        satu_dadu()
    elif pilih == 2:    
        dua_dadu()
    elif pilih == 0:
        break
