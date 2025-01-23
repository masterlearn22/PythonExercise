 
question = (
    ("1. Apa penyebab utama terjadinya Perang Seratus Tahun antara Inggris dan Prancis? "),
    ("2. Siapa yang dikenal sebagai 'Bapak Sejarah' karena karyanya yang mendokumentasikan Perang Persia?"),
    ("3. Apa yang menjadi simbol dari Revolusi Prancis pada tahun 1789?"),
    ("4. Negara mana yang pertama kali menjelajahi jalur laut ke Asia Tenggara pada abad ke-16?"),
    ("5. Apa yang menjadi hasil dari Konferensi Berlin tahun 1884-1885?")
)
options=(
    ("A. Persaingan perdagangan","B. Klaim atas tahta Prancis","C. Perbedaan agama","D. Invasi Viking"),
    ("A. Thucydides","B. Herodotus","C. Plutarch","D. Tacitus"),
    ("A. Penangkapan Bastille","B. Pembunuhan Louis XVI","C. Deklarasi Hak Manusia","D. Pembentukan Republik"),
    ("A. Inggris","B. Spanyol","C. Portugis","D. Belanda"),
    ("A. Pembagian wilayah Afrika di antara negara-negara Eropa","B. Penyelesaian konflik di Balkan","C. Pembentukan Liga Bangsa-Bangsa","D. Pengakuan kemerdekaan Belgia")
    )
answer=(
    "B",
    "B", 
    "A",
    "C",
    "A"
    )

while True:
    print("\nDaftar Pertanyaan Sejarah:")
    for soal in question:
        print("".join(map(str, soal)))
        
    pilih_soal= input("\nMasukkan nomor soal yang ingin Anda jawab (1/2/3/4/5)\n")
    if pilih_soal == "q":
        break
    pilih_soal= int(pilih_soal)
    
    try:
        if 1 <= pilih_soal <= len(question):
            print(f"\n{question[pilih_soal-1]}")
            print("\nPilihan jawaban:")
            for opsi in options[pilih_soal-1]:
                print(opsi)
            
            jawaban_user = input("\nMasukkan jawaban Anda (A/B/C/D): ").upper()
            
            if jawaban_user == answer[pilih_soal-1]:
                print("Selamat! Jawaban Anda benar.")
            else:
                # Konversi huruf jawaban ke indeks
                #ord(answer[pilih_soal-1]) - ord('A')'A' menjadi 0, dst.
                indeks_jawaban = ord(answer[pilih_soal-1]) - ord('A')
                print (indeks_jawaban)
                print(f"Maaf, jawaban yang benar adalah: {options[pilih_soal-1][indeks_jawaban]}")
        else:
            print("Nomor soal tidak valid. Silakan pilih 1-5.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan nomor antara 1-5 atau 'q'.")
        
