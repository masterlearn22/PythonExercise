import random

def spin_row():
    """Menghasilkan baris slot dengan simbol acak."""
    symbols = {
        1: "⚽",
        2: "⚾",
        3: "🏀",
        4: "🏈",
        5: "🏐"
    }
    # Menghasilkan 3 simbol secara acak
    row = [random.randint(1, 5) for _ in range(3)]
    row_symbols = [symbols[i] for i in row]
    return row_symbols

def print_row(row):
    """Menampilkan baris slot."""
    print(" | ".join(row))

def get_payout(row, bet):
    """Menghitung payout berdasarkan hasil spin."""
    if row[0] == row[1] == row[2]:  # Jika semua simbol sama
        print("🎉 Kamu menang! Semua simbol sama! 🎉")
        hadiah= bet*10
        print("Kamu mendapat : ", hadiah)
        return hadiah
    else:
        print("Coba lagi! Kamu belum menang.")
        return 0

def main():
    saldo = 100
    print("┌─────────────────────┐")
    print("│  Selamat datang di  │")
    print("│    SLOT MACHINE     │")
    print("│     ⚽🏀🏐⚾🎱      │")
    print("└─────────────────────┘")
    
    while True:
        print(f"Saldo kamu: Rp {saldo:,}")
        bet = int(input("Masukkan jumlah taruhan: "))
        
        while bet < (10/100*saldo):
            print("Maaf, taruhan minimal adalah 10% dari saldo kamu.")
            bet = int(input("Masukkan jumlah taruhan: "))
        if bet > saldo:
            print("Saldo tidak cukup. Masukkan jumlah yang sesuai.")
            continue
        elif bet <= 0:
            print("Taruhan tidak valid. Masukkan jumlah yang benar.")
            continue

        saldo -= bet
        row = spin_row()
        print("Hasil slot:")
        print_row(row)

        payout = get_payout(row, bet)
        saldo += payout

        if saldo <= 0:
            print("Saldo kamu habis. Game over!")
            break

        lagi = input("Ingin bermain lagi? (y/n): ").lower()
        if lagi != "y":
            break

if __name__ == '__main__':
    main()
