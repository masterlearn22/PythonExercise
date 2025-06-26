import tkinter as tk
from visual import IngredientCheckerApp
import sys

if __name__ == "__main__":
    if 'idlelib' in sys.modules:
        print("MAIN.PY: Aplikasi dijalankan dari IDLE. Pesan print mungkin tidak terlihat setelah GUI ditutup.")
        print("MAIN.PY: Disarankan menjalankan dari terminal untuk melihat semua output debug.")

    print("MAIN.PY: Memulai aplikasi Pengecek Ingredient Nutrisi...") 
    root = tk.Tk()
    app = IngredientCheckerApp(root)
    root.mainloop()
    print("MAIN.PY: Aplikasi ditutup.")