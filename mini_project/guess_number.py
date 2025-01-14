import random

def play_game():
    # Generate a random number between 1 and 100
    num_rand = random.randint(1, 100)
    nyawa = 5

    # Set initial bounds
    lower_bound = 1
    upper_bound = 100

    print("Tebak angka antara 1 dan 100.")

    while True:
        guess_num = int(input(f"Tebak angka (nyawa tersisa: {nyawa}): "))

        if guess_num < lower_bound or guess_num > upper_bound:
            print(f"Tebakan harus berada dalam rentang {lower_bound} - {upper_bound}.")
            continue

        if guess_num < num_rand:
            print(f"{guess_num} terlalu rendah. Coba angka antara {guess_num + 1} dan {upper_bound}.")
            lower_bound = guess_num + 1  # Update the lower bound
            nyawa -= 1
        elif guess_num > num_rand:
            print(f"{guess_num} terlalu tinggi. Coba angka antara {lower_bound} dan {guess_num - 1}.")
            upper_bound = guess_num - 1  # Update the upper bound
            nyawa -= 1
        else:
            print("Selamat, Anda menemukan angka yang benar!")
            break

        if nyawa == 0:
            print("Kamu kalah, angka yang benar adalah:", num_rand)
            # Ask if the player wants to play again
            play_again = input("Apakah Anda ingin bermain lagi? (y/t): ").lower()
            if play_again == 'y':
                play_game()  # Restart the game
            else:
                print("Terima kasih telah bermain!")
            break

# Start the game
play_game()