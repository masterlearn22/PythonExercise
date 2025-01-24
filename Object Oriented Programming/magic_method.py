def materi():
    class buku:
        def __init__(self, judul, penulis, halaman):
            self.judul = judul
            self.penulis = penulis
            self.halaman = halaman

        def __str__(self):
            return f"Judul: {self.judul}\nPenulis: {self.penulis}\nHalaman: {self.halaman}"
        
        def __eq__(self, other):
            return self.judul == other.judul or self.penulis == other.penulis or self.halaman == other.halaman 
        
        def __ne__(self, value):
            return self.judul != value.judul or self.penulis != value.penulis or self.halaman != value.halaman
        
        def __lt__(self, other):
            return self.halaman < other.halaman 
        
        def __gt__(self, other):
            return self.halaman > other.halaman
        
        def __add__(self, other):
            return self.halaman + other.halaman
        
        def __contains__(self, item):
            return item in self.judul or item in self.penulis
        
        def __getitem__(self, key):
            if key == 'judul':
                return self.judul
            elif key == 'penulis':
                return self.penulis
            elif key == 'halaman':
                return self.halaman
            else:
                return "Key tidak ditemukan"
        
        
    buku1 = buku("Python for Data Science", "Surya Dwi Satria", 200)
    buku2 = buku("Atomic Habits Clear", "James Clears", 250)
    buku3 = buku("Atomic Habits", "Morgan Housel", 150)  
    buku4 = buku("The Lean Startup", "Eric Ries", 200)
    buku5 = buku("The Hard Thing About Hard Things", "Ben Horowitz", 220)

    #__str__ method digunakan untuk mengembalikan string yang akan ditampilkan ketika objek tersebut diprint
    for buku in (buku1, buku2, buku3, buku4, buku5):
        print(buku)
        print()
        
    # __eq__ method digunakan untuk membandingkan dua objek
    print("Mencari kesamaan antara kedua buku dari judul, penulis, dan halaman")
    print(buku2 == buku3) # True judul sama
    print(buku1 == buku4) # True halaman sama
    print(buku2 == buku5) # False tidak ada yang sama

    # __ne__ method digunakan untuk membandingkan dua objek
    print("Mencari perbedaan antara kedua buku dari judul, penulis, dan halaman")
    print(buku2 != buku3) # False judul sama
    print(buku1 != buku4) # False halaman sama
    print(buku2 != buku5) # True tidak ada yang sama
    
    #__lt__ method digunakan untuk membandingkan dua objek
    print("Mencari buku dengan halaman paling sedikit")
    print(buku1 < buku2) # True buku1(200) halaman lebih sedikit dari buku2(250)
    print(buku2 < buku5) # False buku2(250) halaman lebih banyak dari buku5 (220)
    print(buku4 < buku5) # True buku4(200) halaman lebih sedikit dari buku5 (220)
    
    #__gt__ method digunakan untuk membandingkan dua objek
    print("Mencari buku dengan halaman paling banyak")
    print(buku1 > buku2) # False buku1(200) halaman lebih sedikit dari buku2(250)
    print(buku2 > buku5) # True buku2(250) halaman lebih banyak dari buku5 (220)
    print(buku4 > buku5) # False buku4(200) halaman lebih sedikit dari buku5 (220)
    
    #__add__ method digunakan untuk menjumlahkan dua objek
    print("Jumlah halaman dari dua buku")
    print(buku1 + buku2) # 450
    print(buku2 + buku5) # 470
    print(buku4 + buku5) # 420
        
    #__contains__ method digunakan untuk mengecek apakah suatu string terdapat dalam atribut dari objek
    print("Mencari kata dalam judul atau penulis")
    print("Python" in buku1) # True
    print(('Clear' or 'Clears') in buku2) # True
    print(("About" and "Ben") in buku5) # True
    print("Atomic Habits" not in buku2) # False
        
    #__getitem__ method digunakan untuk mengakses atribut dari objek
    print("Mengakses atribut dari objek")
    print(buku1['judul']) # Python for Data Science
    print(buku2['penulis']) # James Clears
    print(buku3['halaman']) # 150
    
    
    
materi()