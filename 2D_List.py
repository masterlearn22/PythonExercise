smartphone =["Xiaomi", "Samsung", "Iphone","Vivo", "Oppo"]
laptop = ["Dell", "Lenovo", "HP", "Asus", "Acer"]
smartwatch = ["Huawei", "Apple", "Fossil", "Samsung", "Skagen"]
headphones = ["Sony", "Sennheiser", "JBL", "Beats"]

devices = [smartphone, laptop, smartwatch, headphones]

def cara1():
    print("Ini adalah daftar devices yang tersedia")
    for collection in devices:
        for item in collection:
            print(item, end=" ")
        print(end=",")
        print()
        
def cara2():
    print("Ini adalah daftar devices yang tersedia:")
    for collection in devices:
        print(", ".join(collection)) 

cara2()
print()
# Mengakses elemen dengan lebih ringkas
smartphone_items = [devices[0][i] for i in [0, 2, 3]]  # Mengambil item tertentu dari smartphone
laptop_items = [devices[1][i] for i in [0, 1]]  # Mengambil item tertentu dari laptop
smartwatch_items = [devices[2][i] for i in [0, 2]]  # Mengambil item tertentu dari smartwatch
headphone_items = [devices[3][i] for i in [0, 1]]  # Mengambil item tertentu dari headphones

print(f"Saya ingin beli \nSmartphone : {', '.join(smartphone_items)}")
print(f"Laptop : {', '.join(laptop_items)}")
print(f"Smartwatch : {', '.join(smartwatch_items)}")
print(f"Headphone : {', '.join(headphone_items)}")


       
    
    