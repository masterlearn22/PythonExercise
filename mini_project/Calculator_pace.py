def pace_calculator():
    print("Kalkulator Pace Lari")
    
    # Meminta input jarak
    distance = float(input("Masukkan jarak yang ditempuh (dalam kilometer): "))
    
    # Meminta input waktu
    waktu = input("Masukkan waktu yang dihabiskan (format: jam.menit.detik, tekan Enter untuk 00.00.00): ")
    
    # Memeriksa apakah input waktu kosong
    if not waktu:
        hours, minutes, seconds = 0, 0, 0  # Jika tidak ada input, set waktu ke 0
    else:
        # Menangani format input yang tidak lengkap
        try:
            # Memisahkan jam, menit, dan detik
            parts = list(map(int, waktu.split('.')))
            if len(parts) == 1:
                hours, minutes, seconds = 0, 0, parts[0]  # Hanya detik yang diberikan
            elif len(parts) == 2:
                hours, minutes, seconds = 0, parts[0], parts[1]  # Jam tidak diberikan
            elif len(parts) == 3:
                hours, minutes, seconds = parts  # Semua bagian diberikan
            else:
                raise ValueError("Format waktu tidak valid.")
        except ValueError:
            print("Input waktu tidak valid, menggunakan 00.00.00 sebagai default.")
            hours, minutes, seconds = 0, 0, 0  # Set waktu ke 0 jika terjadi kesalahan
    
    # Menghitung total waktu dalam detik
    total_time_seconds = hours * 3600 + minutes * 60 + seconds
    
    # Menghitung pace dalam detik per kilometer
    pace_seconds_per_km = total_time_seconds / distance
    
    # Menghitung pace dalam menit dan detik
    pace_minutes = int(pace_seconds_per_km // 60)
    pace_seconds = int(pace_seconds_per_km % 60)
    
    # Menampilkan hasil
    print(f"Pace Anda adalah: {pace_minutes}:{pace_seconds:02d}/km.")  # Menampilkan detik dengan dua digit

    
def distance_calculator():
    print("Kalkulator Jarak Lari")
    
    # Meminta input waktu
    waktu = input("Masukkan waktu yang dihabiskan (format: jam.menit.detik, tekan Enter untuk 00.00.00): ")
    
    # Memeriksa apakah input waktu kosong
    if not waktu:
        hours, minutes, seconds = 0, 0, 0  # Jika tidak ada input, set waktu ke 0
    else:
        # Menangani format input yang tidak lengkap
        try:
            # Memisahkan jam, menit, dan detik
            parts = list(map(int, waktu.split('.')))
            if len(parts) == 1:
                hours, minutes, seconds = 0, 0, parts[0]  # Hanya detik yang diberikan
            elif len(parts) == 2:
                hours, minutes, seconds = 0, parts[0], parts[1]  # Jam tidak diberikan
            elif len(parts) == 3:
                hours, minutes, seconds = parts  # Semua bagian diberikan
            else:
                raise ValueError("Format waktu tidak valid.")
        except ValueError:
            print("Input waktu tidak valid, menggunakan 00.00.00 sebagai default.")
            hours, minutes, seconds = 0, 0, 0  # Set waktu ke 0 jika terjadi kesalahan
    total_time_seconds = hours * 3600 + minutes * 60 + seconds
    
    # Meminta input pace
    pace = input("Masukkan pace Anda (format: menit.detik): ")
    
    pace_minutes, pace_seconds = map(float, pace.split('.')) #mengabungkan 2 inputan menjadi 1
    
    # Menghitung total pace dalam detik
    total_pace_seconds = (pace_minutes * 60) + pace_seconds
    
    # Menghitung jarak yang ditempuh
    distance_km = total_time_seconds / total_pace_seconds
    
    # Menampilkan hasil
    print(f"Jarak yang ditempuh adalah: {distance_km:.2f} kilometer.")

def time_calculator():
    print("Kalkulator Waktu Lari")
    
    # Meminta input jarak
    distance = float(input("Masukkan jarak yang ditempuh (dalam kilometer): "))
    
    # Meminta input pace dalam format menit dan detik
    pace_input = input("Masukkan pace Anda (format: menit.detik): ")
    
    # Memisahkan menit dan detik
    pace_minutes, pace_seconds = map(float, pace_input.split('.')) #mengabungkan 2 inputan menjadi 1
    
    # Menghitung total pace dalam detik
    total_pace_seconds = (pace_minutes * 60) + pace_seconds
    
    # Menghitung total waktu dalam detik
    total_time_seconds = total_pace_seconds * distance
    
    # Menghitung jam, menit, dan detik dari total waktu
    hours = int(total_time_seconds // 3600)
    minutes = int((total_time_seconds % 3600) // 60)
    seconds = int(total_time_seconds % 60)
    
    # Menampilkan hasil
    print(f"Waktu yang dibutuhkan adalah: {hours} jam, {minutes} menit, {seconds} detik.")


print("Selamat datang di Kalkulator Lari!")
while True:
    print("Silakan pilih kalkulator yang ingin Anda gunakan:")
    print("1. Kalkulator Waktu Lari")
    print("2. Kalkulator Jarak Lari")
    print("3. Kalkulator Pace Lari")
    choice = int(input("Pilih nomor kalkulator: "))
    if choice == 1:
        time_calculator()
    elif choice == 2:
        distance_calculator()
    elif choice == 3:
        pace_calculator()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
