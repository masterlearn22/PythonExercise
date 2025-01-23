import random
uang = 0
for i in range (1, 11):
    tambahan = random.randint(0, 10000)
    print(f"uang bertambah Rp{tambahan:+,}")
    uang += tambahan

print(f"Jumlah uang saat ini adalah Rp{uang:,}")
    