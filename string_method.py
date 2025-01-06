def mencari_huruf() :  
    while True :
        nama = input("Masukkan nama Anda: ")
        if nama == "exit":
            break
        result = int(nama.find(input("Masukkan huruf yang ingin dicari: "))) +1 # find() mencari huruf yang diinputkan pada variabel "nama"
        print(result)
        
def mengukur_kata():
    while True:
        kalimat = input("Masukkan kalimat yang ingin diukur: ")
        if kalimat == "exit":
            break
        spasi = int(kalimat.count(" ")) # mencari dan menhitung jumlah spasi dari variabel ""kalimat"
        result = len(kalimat) - spasi
        print(result)
        
def struktur_kata():
    while True:
        kalimat = input("Masukkan kalimat yang ingin diuji: ")
        if kalimat == "exit":
            break 
        result = kalimat.capitalize() # mengubah huruf pertama dari kalimat menjadi huruf kapital
        result2 = kalimat.upper() # mengubah semua huruf pada kalimat menjadi huruf kapital
        result3 = kalimat.lower() # mengubah semua huruf pada kalimat menjadi huruf kecil
        result4= kalimat.isdigit() # mengecek apakah kalimat hanya berisi angka atau tidak
        result5= kalimat.isalpha() # mengecek apakah kalimat hanya berisi huruf atau tidak dan tidak mengandung spasi, angka, atau karakter khusus
        result6= kalimat.swapcase() # mengubah huruf kapital menjadi huruf kecil dan sebaliknya
        result7= kalimat.replace(' ','-') # mengubah huruf pertama dari setiap kata menjadi huruf kapital
        print(result)
        print(result2)
        print(result3)
        print(result4)
        print(result5)
        print(result6)
        print(result7)
        print("Jika ingin keluar, ketik 'exit'")
        
def informasi_string_method():
    print("Selamat datang di program string method!")
    print(help(str))
    
def validation() :
    while True :
        print("username tidak boleh mengandung spasi")
        print("password minimal 8 karakter")
        print("password harus mengandung huruf kapital")
        print("password harus mengandung angka")
        print("password harus mengandung karakter khusus")
        
        while True :
            username = input("Masukkan username: ")
            if " " in username :
                print("Username tidak boleh mengandung spasi")
                continue
            else :
                break
        while True :
            password = input("Masukkan password: ")
            if len(password) < 8 :
                print("Password minimal 8 karakter")
                continue
            elif password.islower() :
                print("Password harus mengandung huruf kapital")
                continue
            elif password.isdigit() :
                print("Password harus mengandung angka")
                continue
            elif password.isalnum() :
                print("Password harus mengandung karakter khusus")
                continue
            else :
                print("Username dan password berhasil dibuat")
                print("Username: ", username)
                print("Password: ", password)
                break
     
         
while True:     
    print("Selamat mencoba berbagai macam string method!")
    print("Pilihlah menu yang ingin Anda lakukan:")
    print("1. Mencari huruf")
    print("2. Mengukur kata")
    print("3. Struktur kata")
    print("4. Informasi string method")
    print("5. Testing Validation")
    print("Jika ingin keluar, masukan angka '0' ")
    pilihan = int(input("Masukkan pilihan Anda: "))
    

    if pilihan == 1:
        mencari_huruf()
    elif pilihan == 2:
        mengukur_kata()
    elif pilihan == 3:
        struktur_kata()
    elif pilihan == 4:
        informasi_string_method()
    elif pilihan == 5:
        validation()
    elif pilihan == 0:
        print("Terima kasih telah menggunakan program ini")
        break
    else:
        print("Pilihan tidak tersedia")
    