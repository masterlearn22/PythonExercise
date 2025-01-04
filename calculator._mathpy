def calculator():
    print("Kalkulator Sederhana")
    print("Masukkan '=' untuk menghentikan kalkulator.")
    
    result = 0
    operator = None

    while True:
        if operator is None:
            num1 = float(input("Masukkan angka: "))
        else:
            num1 = result  # Gunakan hasil sebelumnya sebagai angka

        operator = input("Operator (+, -, *, /): ")

        if operator == '=':
            print(f"Hasil akhir: {result}")
            break

        num2 = float(input("Masukkan angka: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
                continue
        else:
            print("Operator tidak valid. Silakan coba lagi.")
            continue

        print(f"Hasil: {result}")

calculator()