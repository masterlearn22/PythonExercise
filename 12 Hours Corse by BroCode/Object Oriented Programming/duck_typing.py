def materi():
    class animals:
        alive = True
        
    class Dog(animals):
       def speak(self):
           print("WOOF!")
           
    class Cat(animals):
        def speak(self):
            print("MEOW!")
            
    class Fish(animals):
        def swim(self):
            print("I'm swimming")
    
    class Bird(animals):
        def fly(self):
            print("I'm flying")
            
    class Duck(animals):
        def speak(self):
            print("QUACK!")
            
    class Car :
        alive = False
        def speak(self):
            print("VROOM VROOM!")
            
    animals = [Dog(), Cat(), Duck(),Car()] #Fish, Bird tidak dimasukkan ke dalam list karena tidak memiliki method speak()  
        
    for animal in animals:
        animal.speak()
        print(animal.alive)

materi()

    
def exercixe():
    class hewan:
        hidup = True

    class omnivora(hewan):
        def __init__(self, buah, daging):
            self.buah = buah
            self.daging = daging

    class karnivora(hewan):
        daging = True

    class herbivora(hewan):
        buah = True

    class kucing(omnivora):

        def info(self):
            if self.buah and self.daging:
                print('Kucing adalah hewan omnivora')
            elif self.daging:
                print('Kucing adalah hewan karnivora')
            elif self.buah:
                print('Kucing adalah hewan herbivora')

    class sapi(herbivora):
        def __init__(self, buah=True, daging=False):
            self.buah = buah
            self.daging = daging

        def info(self):
            print('Sapi adalah hewan herbivora')

    class singa(karnivora):
        def __init__(self, buah=False, daging=True):
            self.buah = buah
            self.daging = daging
            
        def info(self):
            print('Singa adalah hewan karnivora')

    class apel():
        pass

    class jeruk(karnivora):
        pass

    class mangga():

        def info(self):
            print('Mangga adalah hewan')

    # Fungsi untuk memeriksa apakah objek termasuk dalam kategori hewan
    def cek_hewan(obj):
        if isinstance(obj, hewan):
            print(f"{obj.__class__.__name__} adalah hewan.")
            #obj adalah instance dari class hewan atau class turunannya, contoh: kucing, sapi, singa
            #__class__ adalah nama class dari objek tersebut, contoh: kucing, sapi, singa
            #__name__ adalah nama dari class tersebut, contoh: kucing, sapi, singa
        else:
            print(f"{obj.__class__.__name__} bukan hewan.")

    # Contoh penggunaan
    hewan1 = kucing(True, False)
    buah1 = apel()
    buah2 = jeruk()

    print(f"Kucing adalah hewan: {hewan1.info()}")

    # Memeriksa apakah objek termasuk hewan
    cek_hewan(hewan1)  # Output: kucing adalah hewan.
    cek_hewan(buah1)   # Output: apel bukan hewan.
    cek_hewan(buah2)   # Output: jeruk adalah hewan.

    print()

    # Daftar objek
    animals = [kucing(True, True), sapi(), singa(), mangga()] #Objek apel dan jeruk tidak dimasukkan ke dalam list karena tidak memiliki method info()
    for animal in animals:
        animal.info()
        print()

