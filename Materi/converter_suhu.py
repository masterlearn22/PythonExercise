def konversi_suhu():
    print("Kalkulator Konversi Suhu")
    print("Pilih jenis konversi:")
    print("1. Celsius (°C) ke Fahrenheit (°F)")
    print("2. Fahrenheit (°F) ke Celsius (°C)")
    print("3. Celsius (°C) ke Kelvin (K)")
    print("4. Kelvin (K) ke Celsius (°C)")
    print("5. Celsius (°C) ke Reamur (°Re)")
    print("6. Reamur (°Re) ke Celsius (°C)")
    print("7. Fahrenheit (°F) ke Reamur (°Re)")
    print("8. Reamur (°Re) ke Fahrenheit (°F)")
    print("9. Kelvin (K) ke Reamur (°Re)")
    print("10. Reamur (°Re) ke Kelvin (K)")
    print("Masukkan 'q' untuk keluar.")

    while True:
        pilihan = input("Pilih konversi (1-10) atau 'q' untuk keluar: ")

        if pilihan == 'q':
            print("Terima kasih telah menggunakan kalkulator konversi suhu.")
            break

        if pilihan == '1':
            celsius = float(input("Masukkan suhu dalam Celsius (°C): "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius} °C = {fahrenheit:.2f} °F")

        elif pilihan == '2':
            fahrenheit = float(input("Masukkan suhu dalam Fahrenheit (°F): "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit} °F = {celsius:.2f} °C")

        elif pilihan == '3':
            celsius = float(input("Masukkan suhu dalam Celsius (°C): "))
            kelvin = celsius + 273.15
            print(f"{celsius} °C = {kelvin:.2f} K")

        elif pilihan == '4':
            kelvin = float(input("Masukkan suhu dalam Kelvin (K): "))
            celsius = kelvin - 273.15
            print(f"{kelvin} K = {celsius:.2f} °C")

        elif pilihan == '5':
            celsius = float(input("Masukkan suhu dalam Celsius (°C): "))
            reamur = celsius * 4/5
            print(f"{celsius} °C = {reamur:.2f} °Re")

        elif pilihan == '6':
            reamur = float(input("Masukkan suhu dalam Reamur (°Re): "))
            celsius = reamur * 5/4
            print(f"{reamur} °Re = {celsius:.2f} °C")

        elif pilihan == '7':
            fahrenheit = float(input("Masukkan suhu dalam Fahrenheit (°F): "))
            reamur = (fahrenheit - 32) * 4/9
            print(f"{fahrenheit} °F = {reamur:.2f} °Re")

        elif pilihan == '8':
            reamur = float(input("Masukkan suhu dalam Reamur (°Re): "))
            fahrenheit = (reamur * 9/4) + 32
            print(f"{reamur} °Re = {fahrenheit:.2f} °F")

        elif pilihan == '9':
            kelvin = float(input("Masukkan suhu dalam Kelvin (K): "))
            reamur = (kelvin - 273.15) * 4/5
            print(f"{kelvin} K = {reamur:.2f} °Re")

        elif pilihan == '10':
            reamur = float(input("Masukkan suhu dalam Reamur (°Re): "))
            kelvin = (reamur * 5/4) + 273.15
            print(f"{reamur} °Re = {kelvin:.2f} K")

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

konversi_suhu()