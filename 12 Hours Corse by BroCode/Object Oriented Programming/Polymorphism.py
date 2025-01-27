class shape :
    def __init__(self):
        pass
    def area(self):
        pass
    
class rectangle(shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    
class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    
class ban(circle):
    def __init__(self,nama, radius):
        super().__init__(radius)
        self.nama = nama
    def area(self):
        return 3.14 * self.radius * self.radius
    
class papan_tulis(rectangle):
    def __init__(self,nama,panjang, lebar):
        super().__init__(panjang, lebar)
        self.nama = nama
    def area(self):
        return self.length * self.breadth

# Membuat objek dari kelas rectangle
shapes =[rectangle(10, 20), circle(15), triangle(10, 20),ban('Maspion', 10), papan_tulis('Sandie', 10, 20)]

for shape_obj in shapes:
    if isinstance(shape_obj, (ban, papan_tulis)): # Jika objek adalah kelas `ban` dan `papan_tulis`
        if isinstance(shape_obj, ban):
            print(f"Ban {shape_obj.nama} memiliki luas {shape_obj.area()} cm²")
        elif isinstance(shape_obj, papan_tulis):
            print(f"Papan Tulis {shape_obj.nama} memiliki luas {shape_obj.area()} cm²")
    else:  # Untuk objek lainnya
        print(f"Objek {type(shape_obj).__name__} memiliki luas {shape_obj.area()} cm²") 
        # type digunakan untuk mendapatkan nama kelas dari objek
        # __name__ digunakan untuk mendapatkan nama kelas dari objek