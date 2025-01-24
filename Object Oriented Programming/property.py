def materi():
    class Circle:
        def __init__(self, radius):
            self.__radius = radius

        @property
        def radius(self):
            return f"{self.__radius:.1f} cm"

        @radius.setter
        def radius(self, new_radius):
            if new_radius > 0:
                self.__radius = new_radius
            else:
                print("Radius harus lebih besar dari 0")

        @property
        def area(self):
            return 3.1415 * (self.__radius ** 2)
        
        @radius.deleter
        def radius(self):
            del self.__radius

    # Membuat objek lingkaran dengan radius awal 5
    c = Circle(5)
    print(f"Radius awal: {c.radius}")  # Mengakses radius awal
    print(f"Luas awal: {c.area:.2f} cm²")  # Mengakses area awal

    # Mengubah radius menjadi 10
    c.radius = 10
    print(f"Radius baru: {c.radius}")
    print(f"Luas baru: {c.area:.2f} cm²")

    # Mencoba memberikan radius negatif
    c.radius = -5  # Akan memberikan pesan error
    print(f"Radius setelah input negatif: {c.radius}")
    
    # Menghapus radius
    del c.radius
    #print(c.radius)  # Akan memberikan pesan error
    c.radius = 12
    print(f"Radius setelah dihapus: {c.radius}")


materi()
