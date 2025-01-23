genap =[item*2 for item in range(1,11,2)]
print(genap)

ganjil=[item for item in range(1,11)]
print(ganjil)

kuadrat = [num * num for num in range(1, 11)]
print(" | ".join(map(str, kuadrat)))

string=[item for item in ("Surya")]
print(string, end=" ")

print()
buahs=["Semangka","Ubi","Rambutan","Yery","Apel"]
d_buah=[buah[0] for buah in buahs]
print(d_buah)

print()
import random
numbers = [random.randint(-20, 20) for _ in range(10)]
print("semua angka:", numbers)
positive = [num for num in numbers if num >= 0]
negative = [num for num in numbers if num <= 0]
print("Positive Numbers:", positive)
print("Negative Numbers:", negative)
