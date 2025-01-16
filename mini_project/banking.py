# Saldo awal
# balance = int(input("Masukkan Jumlah saldo : Rp "))


def show_balance(balance):
    """Menampilkan saldo saat ini."""
    print(f"Saldo : Rp {balance:,}")

def deposit(balance):
    """Menambahkan uang ke saldo."""
      # Mengakses variabel global
    amount = float(input("Deposito : Rp "))
    balance += amount
    print(f"Deposito : Rp {amount:,}. \nSaldo saat ini : Rp {balance:,}")

def withdraw(balance):
    """Mengurangi uang dari saldo."""
      # Mengakses variabel global
    amount = float(input("Masukkan Jumlah Tarik Saldo: Rp "))
    if amount > balance:
        print("Uang tidak cukup ")
    else:
        balance -= amount
        print(f"Jumlah Saldo Ditarik : Rp {amount:,} \nSaldo saat ini : Rp {balance:,}")


            
if __name__ == "__main__":
    def main():
        balance=1000000
        # Program utama
        while True: 
            print("┌─────────────────────┐")
            print("│  Selamat datang di  │")
            print("│   Banking Program   │")
            print("│                     │")   
            print("│   1. Saldo          │")
            print("│   2. Deposito       │")
            print("│   3. Tarik Saldo    │")
            print("│   4. Keluar         │")
            print("└─────────────────────┘")

            pilih = int(input("Pilih program yang ingin kamu jalankan: "))
            if pilih == 1:
                print("-----Tampilan Saldo-----")
                show_balance(balance)
            elif pilih == 2:
                print("-----Tampilan Deposito-----")
                deposit(balance)
            elif pilih == 3:
                print("-----Tampilan Tarik Saldo-----")
                withdraw(balance)
            elif pilih == 4:
                break
            else:
                print("Pilihan tidak tersedia. Pilih program yang tersedia.")
    main()