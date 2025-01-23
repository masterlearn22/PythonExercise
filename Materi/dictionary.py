CC ={
    "Indonesia":"Jakarta",
    "USA":"Washington D.C.",
    "China":"Beijing",
    "Japan":"Tokyo",
    "South Korea":"Seoul",
}
print(" ".join(CC))

def testing():
    while True:
        newCountry= input("Masukkan negara : ")

        if newCountry not in CC:
            print("Negara tidak ditemukan")
            newCapital= input("Masukkan ibu kota baru :")
            CC[newCountry]=newCapital
            print(" ".join(CC))
        elif newCountry == "q":
            break
        if newCountry in CC:
            print(CC.get(newCountry)) 
            
def exercise():
    CC = {
    "Indonesia": "Jakarta",
    "United States": "Washington D.C.",
    "China": "Beijing",
    "Japan": "Tokyo",
    "South Korea": "Seoul",
}

while True:
    newCountry = input("Masukkan negara (atau 'q' untuk keluar): ")

    if newCountry.lower() == "q":
        print("\nDaftar Negara dan Ibu Kota:")
        for country, capital in CC.items():
            print(f"{country:14}: {capital}")
        break

    if newCountry not in CC:
        print("Negara tidak ditemukan.")
        newCapital = input("Masukkan ibu kota baru: ")
        CC.update({newCountry:newCapital}) # Add new country and capital
        print(f"Negara {newCountry} dengan ibu kota {newCapital} telah ditambahkan.")
        print(" ".join(CC))
    else:
        print(f"Ibu kota {newCountry} adalah {CC[newCountry]}.")
        
        while True:
            pilih = input("Perbarui atau hapus ibu kota? (y/t/h): ")
            if len(pilih) != 1 or pilih.lower() not in ['y', 't','h']:
                print("Pilihan tidak valid. Silakan masukkan 'y' atau 't'.")
                continue
            
            if pilih.lower() == "y":
                newCapital = input("Masukkan ibu kota baru: ")
                CC.update({newCountry:newCapital})  # Update the capital
                print(f"Ibu kota {newCountry} telah diperbarui menjadi {newCapital}.")
                break  # Exit the inner loop after updating
            elif pilih.lower() == "t":
                break  # Exit the inner loop without updating
            elif pilih.lower() == "h":
                print(f"Negara {newCountry} telah dihapus dari daftar.") # Delete the country
                CC.pop(newCountry)
                break
     
exercise()
        