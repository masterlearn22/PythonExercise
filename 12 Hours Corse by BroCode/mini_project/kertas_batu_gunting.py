import random
lawan ={1:"kertas", 2:"batu", 3:"gunting"}
kawan ={1:"kertas", 2:"batu", 3:"gunting"}
def tebak_tangan():
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

tebak_tangan()
while True: 
    if input("apakah kamu ingin bermain? (y/n) : ") == "y":
        tebak_tangan()
    elif "n":
        break

