
uang = 1000000
omset = 500000
uang_saat_ini = uang + omset

print(f"Uang saya sekarang Rp{uang:,.2f}") # Output: Uang saya sekarang Rp1,000,000.00 -> , untuk pemisah ribuan dan . untuk pemisah desimal 2 digit
print(f"Omset saya sekarang Rp{omset:+,.5f}") # Output: Omset saya sekarang Rp+500
print(f"Uang saya sekarang Rp{uang_saat_ini:,.2f}") # Output: Uang saya sekarang Rp1,500,000.00

