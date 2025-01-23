def single_dial():  
    num_pad = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ("*", 0, "#")
    )

    # Menampilkan num_pad
    for dial in num_pad:
        print(" ".join(map(str, dial)))

    # Membuat daftar semua nilai valid dari num_pad
    valid_inputs = [str(item) for sublist in num_pad for item in sublist]

    # List untuk menyimpan input pengguna
    dialed_numbers = []

    while True:
        user_input = input("dial (press Enter to exit): ")
        
        # Memeriksa apakah input kosong untuk keluar dari loop
        if user_input == "":
            print("Exiting dial...")
            break
        
        # Memeriksa apakah input valid
        if user_input not in valid_inputs:
            print("Masukkan dial yang benar.")
            continue  # Kembali ke awal loop jika input tidak valid

        # Menyimpan input yang valid
        dialed_numbers.append(user_input)

    # Menampilkan hasil akhir dial
    if dialed_numbers:
        print(f"Hasil akhir dial Anda: {''.join(dialed_numbers)}")
    else:
        print("Tidak ada dial yang dimasukkan.")
        
def multi_dial() :
    num_pad = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ("*", 0, "#")
    )

    # Menampilkan num_pad
    for dial in num_pad:
        print(" ".join(map(str, dial)))

    # Membuat daftar semua nilai valid dari num_pad
    valid_inputs = [str(item) for sublist in num_pad for item in sublist]
    #valid_inputs adalah variabel list comprehension dalam bentuk stting
    #sublist -> (1,2,3) and (4,5,6) and (7,8,9) and ('*',0,'#')
    #item -> 1,2,3 berasal dari sublist[0](1,2,3)
    
    print(f"ini adalah bentuk dari valid inputs : {valid_inputs}")

    # List untuk menyimpan input pengguna
    dialed_numbers = []

    while True:
        user_input = input("Dial (press Enter to exit): ")
        
        # Memeriksa apakah input kosong untuk keluar dari loop
        if user_input == "":
            print("Exiting dial...")
            break
        
        # Memeriksa apakah semua karakter user_input sudah sesuai dengan valid_inputs
        #char in valid_inputs -> 1,2,3,4,5,6,7,8,9,'*',
        if all(char in valid_inputs for char in user_input):
            # Menyimpan input yang valid
            dialed_numbers.extend(user_input)  # Menambahkan semua karakter ke dalam dialed_numbers
            print(f"You dialed: {user_input}")
        else:
            print("Masukkan dial yang benar.")

    # Menampilkan hasil akhir dial
    if dialed_numbers:
        print(f"Hasil akhir dial Anda: {''.join(dialed_numbers)}")
    else:
        print("Tidak ada dial yang dimasukkan.")
    
    
print("pilih dial yang ingin digunakan")
print("1. single dial (hanya bisa input satu satu saat memasukkan dial)")
print("2. multi dial (bisa memasukkan beberapa dial sekaligus saat input)")
pilihan = input("masukkan pilihan: ")
if pilihan == "1":
    single_dial()
elif pilihan == "2":
    multi_dial()
    