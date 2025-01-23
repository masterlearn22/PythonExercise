#slicing = membuat substring dari string yang lebih besar contoh: indexing [start:stop:step] or slicng(start, stop, step) 

name = "Surya Dwi Satria"

first_name = name[:5] #Outputnya = Surya
middle_name = name[6:9] #Outputnya = Dwi
last_name = name[10:] #Outputnya = Satria
reverse_name = name[::-1] #Outputnya = airtaS iwD ayrus
jarak_name = name[::3] #Outputnya = SraD tia jadi akan menampilkan tiap `3` huruf

print(first_name)
print(middle_name)
print(last_name)
print(reverse_name)
print(jarak_name)

url1 ="http://tokopedia.com"
url2 ="http://bukalapak.com"
url3 ="http://shopee.com"

url= slice(7,-4) #digunakan untuk mengambil bagian dari string yang diinginkan

print(url1[url])
print(url2[url])
print(url3[url])
