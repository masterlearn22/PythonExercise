import banking

# Cobalah mengimpor fungsi tanpa menjalankan program utama
# banking.main() # tidak bisa dijalankan, karena di dalam if __name__ == "__main__":
# Cobalah menjalankan fungsi lain

#ini hanya digunakan untuk testing banking saja, tidak benar benar menggunakan main fungsi yang menjalankan saldo secara real time
banking.show_balance(100000) # bisa dijalankan, karena tidak ada if __name__ == "__,  --> jumlah saldo sesuai parameter yang dipanggil
banking.deposit(100000) # bisa dijalankan, karena tidak ada if __name__ == "__ , --> jumlah saldo sesuai parameter yang dipanggil
banking.withdraw(100000) # bisa dijalankan, karena tidak ada if __name__ == "__,--> jumlah saldo sesuai parameter yang dipanggil
