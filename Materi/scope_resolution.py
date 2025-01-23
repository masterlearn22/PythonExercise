#SCOPE RESOLUTION = (LEGB) -->> Local -> Enclosed -> Global -> Built-in
# 1. Apa itu LEGB?
# LEGB adalah aturan pencarian variabel di Python berdasarkan urutan hierarki berikut:
# L - Local: Variabel yang didefinisikan di dalam fungsi saat ini.
# E - Enclosed: Variabel yang didefinisikan dalam fungsi luar (fungsi yang membungkus fungsi lain).
# G - Global: Variabel yang didefinisikan di luar fungsi, pada tingkat modul.
# B - Built-in: Variabel atau fungsi bawaan Python seperti len, print, math.pi, dll.

# Local Scope
def local():
    local_variabel = 35  # Didefinisikan di dalam fungsi
    print(f"{'Local':10} = {local_variabel}")
local()

# Enclosed Scope
def enclosed():
    local_variabel = 50  # Didefinisikan di fungsi luar
    def enclosed2():
        print(f"{'Enclosed':10} = {local_variabel}")  # Akses dari fungsi dalam
    enclosed2()
enclosed()

# Global Scope
global_variabel = 45  # Didefinisikan di luar fungsi
def globals():
    print(f"{'Global':10} = {global_variabel}")
globals()

# Built-in Scope
import math
def built_in():
    print(f"{'Built-in':10} = {math.pi}")  # Mengakses variabel built-in
built_in()

