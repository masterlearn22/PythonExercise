import time

waktuku =int(input("Masukkan waktu sekarang : "))

for x in range(waktuku,0,-1) :
    detik = x % 60
    menit = int(x / 60) % 60
    jam = int(x / 3600)
    print(f"{jam:02}:{menit:02}:{detik:02}")
    time.sleep(1) #memberi jeda output sebanyak 1 detik
    
print("Waktu Habis")