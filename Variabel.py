
#STRING
nama = "Surya"
alamat = "Jl. Dharmawangsa VII"
print(nama)
print(f"Namaku {nama} aku sekarang tinggal di {alamat}")


#INTEGER
age = 20
born= 22-12-2004
print(f"Umurku {age} aku lahir pada tanggal {born}")


#FLOAT
tinggi = 180.5
berat = 70.5
print(f"Aku memiliki tinggi {tinggi} dan berat {berat}")

#BOOLEAN dan mengubah jenis data menggunakan if condition
menikah = False
if(menikah == 0):
     menikah = "belum"
else:
    menikah = "sudah"

print(f"Status menikahku {menikah}")

#LIST
hobi = "Membaca", "Menulis", "Menggambar"
print(f"Hobiku adalah {hobi}")

#DICTIONARY
data = {"Nama": "Surya", "Umur": 20, "Alamat": "Jl. Dharmawangsa VII"}
print(f"Namaku {data['Nama']} umurku {data['Umur']} dan alamatku {data['Alamat']}")

#TUPLE
buah = ("Apel", "Jeruk", "Mangga")
print(f"Buah-buahan yang aku sukai adalah {buah}")

#SET
warna = {"Merah", "Kuning", "Hijau"}
print(f"Warna kesukaanku adalah {warna}")

#FROZENSET
kendaraan = frozenset(["Motor", "Mobil", "Sepeda"])
print(f"Kendaraan yang aku miliki adalah {kendaraan}")

#RANGE
angka = range(10)
print(f"Angka yang aku punya adalah {angka}")

#NONE
kosong = None
print(f"Variabel kosong {kosong}")

#BYTES
data = b"Hello"
print(f"Data bytes {data}")

#BYTEARRAY
data = bytearray(5)
print(f"Data bytearray {data}")

#MEMORYVIEW
data = memoryview(bytes(5))
print(f"Data memoryview {data}")

#LIST COMPREHENSION x=0,1,2,3,4,5,6,7,8,9 -> x^2
data = [x**2 for x in range(10)]
print(f"List Comprehension {data}")

#SET COMPREHENSION  
data = {x**2 for x in range(10)}
print(f"Set Comprehension {data}")

#DICTIONARY COMPREHENSION
data = {x: x**2 for x in range(20)}
print(f"Dictionary Comprehension {data}")

#GENERATOR EXPRESSION
data = (x**2 for x in range(10))
print(f"Generator Expression {data}")

#LAMBDA FUNCTION
data = lambda x: x**2 
print(f"Lambda Function {data(10)}") #10^2 = 100 -> x**10

#ANONYMOUS FUNCTION
data = map(lambda x: x**2, range(10))
print(f"Anonymous Function {list(data)}")

#GLOBAL VARIABLE
x = "global"
def myfunc():
    global x
    x = "local"
myfunc()
print(f"Global Variable {x}")


#NONLOCAL VARIABLE
def myfunc():
    z = "local"
    def myinnerfunc():
        nonlocal z
        z = "nonlocal"
    myinnerfunc()
    print(f"Nonlocal Variable {z}")
    
myfunc()

#STRING FORMAT
nama = "Surya"
umur = 20
print("Nama saya adalah {} dan umur saya adalah {}".format(nama, umur))
print(f"Nama saya adalah {nama} dan umur saya adalah {umur}")

#STRING METHOD
text = "Hello World"
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("H", "J"))
print(text.split())
print(text.capitalize())
print(text.casefold())
print(text.center(20))
print(text.encode())
print(text.endswith("d"))
print(text.find("W"))
print(text.index("W"))
print(text.isalnum())
print(text.isalpha())
print(text.isascii())
print(text.isdecimal())
print(text.isdigit())
print(text.isidentifier())
print(text.islower())
print(text.isnumeric())
print(text.isprintable())
print(text.isspace())
print(text.istitle())
print(text.isupper())
print(text.join("H"))
print(text.ljust(20))
print(text.lstrip())
print(text.partition("W"))
print(text.rfind("W"))
print(text.rindex("W"))
print(text.rjust(20))
print(text.rsplit())
print(text.rstrip())
print(text.splitlines())
print(text.startswith("H"))
print(text.swapcase())
print(text.title())
print(text.zfill(20))

#LIST METHOD
buah = ["Apel", "Jeruk", "Mangga"]
buah.append("Pisang")
print(buah)
buah.clear()
print(buah)
buah = ["Apel", "Jeruk", "Mangga"]
buah1 = buah.copy()
print(buah1)
print(buah.count("Apel"))
buah.extend(buah1)
print(buah)
print(buah.index("Jeruk"))
buah.insert(1, "Pisang")
print(buah)
buah.pop()
print(buah)
buah.remove("Apel")
print(buah)
buah.reverse()
print(buah)
buah.sort()
print(buah)

#DICTIONARY METHOD
data = {"Nama": "Surya", "Umur": 20, "Alamat": "Jl. Dharmawangsa VII"}
print(data)
print(data.copy())
