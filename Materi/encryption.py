import random
import string

char = string.ascii_letters  + string.digits + " " + string.punctuation
char =list(char)
kunci= char.copy()

random.shuffle(kunci)
# print(f"{'Character':10}{char}")
# print(f"{"Kunci":10}{kunci}")

while True :
    text = input("Masukkan teks yang ingin di encrypty: ")
    encryption_text = ""

    for i in text:
        index = char.index(i)
        encryption_text += kunci[index] + kunci[index+10] + kunci[index+20] + kunci[index+30]

    print(f"{"Encyrption Text":15} : {encryption_text}")
    # pilih =input()

