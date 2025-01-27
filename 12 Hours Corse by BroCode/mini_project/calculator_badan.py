def konversi_massa():
    print("Kalkulator Konversi Massa")
    print("Pilih jenis konversi:")
    print("1. Kilogram (kg) ke Pound (lbs)")
    print("2. Pound (lbs) ke Kilogram (kg)")
    print("3. Gram (g) ke Miligram (mg)")
    print("4. Miligram (mg) ke Gram (g)")
    print("5. Kilogram (kg) ke Gram (g)")
    print("6. Gram (g) ke Kilogram (kg)")
    print("7. Kilogram (kg) ke Ons (oz)")
    print("8. Ons (oz) ke Kilogram (kg)")
    print("9. Ton (ton) ke Kilogram (kg)")
    print("10. Kilogram (kg) ke Ton (ton)")
    print("Masukkan 'q' untuk keluar.")

    while True:
        pilihan = input("Pilih konversi (1-10) atau 'q' untuk keluar: ")

        if pilihan == 'q':
            print("Terima kasih telah menggunakan kalkulator konversi massa.")
            break

        if pilihan == '1':
            kg = float(input("Masukkan massa dalam kilogram (kg): "))
            lbs = kg * 2.205
            print(f"{kg} kg = {lbs:.2f} lbs")

        elif pilihan == '2':
            lbs = float(input("Masukkan massa dalam pound (lbs): "))
            kg = lbs / 2.205
            print(f"{lbs} lbs = {kg:.2f} kg")

        elif pilihan == '3':
            g = float(input("Masukkan massa dalam gram (g): "))
            mg = g * 1000
            print(f"{g} g = {mg:.2f} mg")

        elif pilihan == '4':
            mg = float(input("Masukkan massa dalam miligram (mg): "))
            g = mg / 1000
            print(f"{mg} mg = {g:.2f} g")

        elif pilihan == '5':
            kg = float(input("Masukkan massa dalam kilogram (kg): "))
            g = kg * 1000
            print(f"{kg} kg = {g:.2f} g")

        elif pilihan == '6':
            g = float(input("Masukkan massa dalam gram (g): "))
            kg = g / 1000
            print(f"{g} g = {kg:.2f} kg")

        elif pilihan == '7':
            kg = float(input("Masukkan massa dalam kilogram (kg): "))
            oz = kg * 35.274
            print(f"{kg} kg = {oz:.2f} oz")

        elif pilihan == '8':
            oz = float(input("Masukkan massa dalam ons (oz): "))
            kg = oz / 35.274
            print(f"{oz} oz = {kg:.2f} kg")

        elif pilihan == '9':
            ton = float(input("Masukkan massa dalam ton (ton): "))
            kg = ton * 1000
            print(f"{ton} ton = {kg:.2f} kg")

        elif pilihan == '10':
            kg = float(input("Masukkan massa dalam kilogram (kg): "))
            ton = kg / 1000
            print(f"{kg} kg = {ton:.2f} ton")

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

konversi_massa()