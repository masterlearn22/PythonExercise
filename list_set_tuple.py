devices =["xiaomi", "samsung", "huawei", "vivo", "oppo"] #list -> urut dan bisa diubah
buahan = {"apel", "mangga", "pisang", "jeruk", "anggur"} # set-> tidak urut dan tidak bisa diubah, bisa menambah/hapus
mobil = ("honda", "ferarri","bugati", "toyota", "nissan") #tuple -> urut tidak bisa di ubah
print (devices)
devices.append("iphone")
devices.insert(2,"nokia")
devices.remove("oppo")
devices.sort()
for device in devices:
    print(device)
print()  

print(buahan)
for buah in buahan:
    print(buah)
print()  
    
print(mobil)
for mobil in mobil:
    print(mobil)