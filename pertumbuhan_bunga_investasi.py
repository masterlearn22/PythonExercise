principle= int(input("Masukkan jumlah uang yang diinvestasikan: "))
rate= float(input("Masukkan tingkat bunga: "))
time= int(input("Masukkan jangka waktu investasi: "))
# Menghitung nilai investasi
while principle < 0 or rate < 0 or time < 0:
    print("Nilai tidak boleh negatif")
    principle= int(input("Masukkan jumlah uang yang diinvestasikan: "))
    rate= float(input("Masukkan tingkat bunga: "))
    time= int(input("Masukkan jangka waktu investasi: "))

future_value= principle* pow((1+rate/100),time)
print(f"Nilai investasi anda setelah {time} tahun adalah: Rp {future_value:,.0f}") #format rupiah