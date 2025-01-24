
def arg_saja():
    def rumah(func):
        def wrapper(*args):
            print("Aku di rumah 🏠")
            func(*args)
        return wrapper


    def kebun(func):
        def wrapper(*args):
            print("Aku di kebun 🌳")
            func(*args)
        return wrapper


    @rumah
    @kebun
    def makanan(*buah):
        print(f"Aku mau makan buah: {', '.join(buah)} 🍎")


    # Memanggil fungsi dengan banyak buah
    makanan("apel", "pisang", "mangga", "jeruk")
    
arg_saja()


# jadi ketika ingin memanggil kotak paling kecil, kita harus membuka terlebih dahulu kotak paling besar?
# Tepat sekali! 🎉 Kalau mau sampai ke kotak paling kecil, kamu harus buka kotak paling besar dulu. 
# Alurnya memang seperti itu, dari luar ke dalam. 
# Jadi, dekorator bekerja seperti lapisan-lapisan pembungkus yang harus dieksekusi dulu sebelum fungsi aslinya dijalankan.

def kwarg_saja():
    def rumah(func):
        def wrapper(**kwargs):
            print("Aku di rumah 🏠")
            func(**kwargs)
        return wrapper


    def kebun(func):
        def wrapper(**kwargs):
            print("Aku di kebun 🌳")
            func(**kwargs)
        return wrapper


    @rumah
    @kebun
    def makanan(**buah):
        print(f"Aku mau makan buah: {', '.join(buah.values())} 🍎")


    # Memanggil fungsi dengan banyak buah
    makanan(buah1="apel", buah2="pisang", buah3="mangga", buah4="jeruk")
    
kwarg_saja()


def arg_kwarg():
    def rumah(func):
        def wrapper(*args, **kwargs):
            print("Aku di rumah 🏠")
            func(*args, **kwargs)
        return wrapper
    def kebun(func):
        def wrapper(*args, **kwargs):
            print("Aku di kebun 🌳")
            func(*args, **kwargs)
        return wrapper
    @rumah
    @kebun
    def makanan(*args, **kwargs):
        print("Buah yang ingin dimakan:")
        for buah in args:
            print(f"- {buah}")
        
        print("\nDetail buah:")
        for nama, jumlah in kwargs.items():
            print(f"{nama}: {jumlah} buah")
        
    # Memanggil fungsi dengan banyak buah
    makanan("apel", "pisang", "mangga", "jeruk", apel = 3, pisang =4, mangga=2, jeruk=1)
              
arg_kwarg()