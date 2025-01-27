#exception = adalah keadaan dimana program tidak berjalan sesuai dengan yang diharapkan
            #1. ZeroDivisionError = terjadi ketika kita membagi angka dengan nol
            #2. ImportError = terjadi ketika import modul yang tidak ada
            #3. ValueError = terjadi ketika fungsi menerima argumen dengan tipe
            #4. FileNotFoundError = terjadi ketika file yang diakses tidak ditemukan
            #5. TypeError = terjadi ketika tipe data yang dioperasikan tidak cocok
            #6. NameError = terjadi ketika variabel tidak ditemukan
            #7. IndexError = terjadi ketika index diluar batas
            #8. KeyError = terjadi ketika key tidak ditemukan
            #9. AttributeError = terjadi ketika atribut tidak ditemukan
            #10. SyntaxError = terjadi ketika ada kesalahan sintaks
            #11. IndentationError = terjadi ketika ada kesalahan indentasi
            #12. RuntimeError = terjadi ketika kesalahan yang terjadi saat runtime
            #13. MemoryError = terjadi ketika kekurangan memori
            #14. KeyboardInterrupt = terjadi ketika pengguna menghentikan program
            #15. OverflowError = terjadi ketika hasil perhitungan terlalu besar
            #dll      
# exception handling = adalah cara untuk mengatasi exception
# 1. try = blok kode yang akan diuji
# 2. except = blok kode yang akan dijalankan jika terjadi exception
# 3. finally = blok kode yang akan dijalankan jika terjadi exception atau tidak

#contoh
#1. ZeroDivisionError
try:
    print(10/0)
except :
    print("tidak bisa membagi angka dengan nol")
finally:
    print("program selesai")
    
#2. ImportError
try:
    import modul
except :
    print("modul tidak ditemukan")
finally:
    print("program selesai")
    
#3. ValueError
try:
    print(int("a"))
except :
    print("nilai harus angka")
finally:
    print("program selesai")
    
#4. FileNotFoundError
try:
    file = open("file.txt")
except :
    print("file tidak ditemukan")
finally:
    print("program selesai")
    
#5. TypeError
try:
    print("10"+10)
except :
    print("tipe data harus sama")
finally:
    print("program selesai")
    
#6. NameError
try:
    print(a)
except :
    print("variabel tidak ditemukan")
finally:
    print("program selesai")
    
#7. IndexError
try:
    a = [1,2,3]
    print(a[3])
except :
    print("index diluar batas")
finally:
    print("program selesai")
    
#8. KeyError
try:
    a = {"nama":"andi"}
    print(a["umur"])
except :
    print("key tidak ditemukan")
finally:
    print("program selesai")
    
#9. AttributeError
try:
    a = [1,4,3]
    a.append(2)
    print(a)
except :
    print("atribut tidak ditemukan")
finally:
    print("program selesai")
    
#10. SyntaxError
try:
    #print("hello" -> SYNTAX ERROR
    print("world")
except :
    print("kesalahan sintaks")
finally:
    print("program selesai")
    
#11. IndentationError
try:
    print("hello")
    #print("world") -> INDENTATION ERROR
except :
    print("kesalahan indentasi")
finally:
    print("program selesai")
    
#12. RuntimeError
try:
    print(10/0)
except :
    print("terjadi kesalahan")
finally:
    print("program selesai")
    
#13. MemoryError
try:
    # a = [1]
    # while True:
    #     a = a+a
    print("Syntax di atas jika di jalankan akan menghasilkan MemoryError")
except :
    print("kekurangan memori")
finally:
    print("program selesai")
    
#14. KeyboardInterrupt
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     print("program dihentikan")
# finally:
#     print("program selesai")
    
#15. OverflowError
try:
    print(10**1000000)
except :
    print("hasil perhitungan terlalu besar")
finally:
    print("program selesai")
    
