import random

animals = (
    "lion", "tiger", "elephant", "giraffe", "zebra", 
    "kangaroo", "panda", "penguin", "dolphin", "whale", 
    "eagle", "owl", "shark", "cheetah", "wolf", 
    "bear", "rabbit", "snake", "frog", "turtle"
)

ques = random.choice(animals)
nyawa = 5
guessed_letters = set() #untuk menyimpan huruf yang sudah ditebak
progress = ["_" for _ in ques]
print(ques)

print(" ".join(progress))

while nyawa > 0:
    if "_" not in progress:
        print("Kamu menang! Kata tersebut adalah:", ques)
        break

    guess = input("Tebak (1 huruf): ").lower()
    while len(guess) != 1 or not guess.isalpha(): #isalpha () untuk memeriksa apakah string hanya berisi huruf
        guess = input("Masukkan 1 huruf yang valid: ").lower()

    if guess in guessed_letters:
        print("Huruf ini sudah ditebak sebelumnya.")
    elif guess in ques:
        print("Benar!")
        guessed_letters.add(guess)
        for idx, letter in enumerate(ques):
            if letter == guess:
                progress[idx] = guess
                # enumerate () untuk mendapatkan index dan nilai dari setiap item dalam list 
                #  idx = letter, misal lion --> 0=l 1=i 2=o 3=n
                #progress adalah daftar yang menunjukkan huruf-huruf yang sudah benar ditebak 
                # misal = lion -> idx 0 = l, idx 1 = i, idx 2 = o, idx 3 = n
                # karena i == guess maka progress[1] = i
                # (jika guess = i) _ i _ _ jika baru huruf "i" yang benar).
    else:
        print("Salah!")
        guessed_letters.add(guess)
        nyawa -= 1

    print("Progress:", " ".join(progress))
    print(f"Nyawa tersisa: {nyawa}")

if nyawa == 0:
    print("Kamu kalah! Kata tersebut adalah:", ques)
