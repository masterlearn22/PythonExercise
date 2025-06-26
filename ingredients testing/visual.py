import tkinter as tk
from tkinter import ttk, messagebox
from logic import hitung_skor_kesehatan
import traceback

class IngredientCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pengecek Ingredient Nutrisi (Fuzzy Mamdani)")
        # Mengembalikan tinggi window untuk mengakomodasi input baru
        self.root.geometry("600x610") 

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", font=("Helvetica", 10))
        style.configure("TButton", font=("Helvetica", 10, "bold"), padding=5)
        style.configure("TEntry", font=("Helvetica", 10), padding=5)
        style.configure("Header.TLabel", font=("Helvetica", 14, "bold"))
        style.configure("Result.TLabel", font=("Helvetica", 12, "bold"))
        style.configure("Info.TLabel", font=("Helvetica", 9))
        style.configure("RangeInfo.TLabel", font=("Helvetica", 8, "italic"), foreground="gray")
        style.configure("Category.TLabel", font=("Helvetica", 9, "italic"))
        style.configure("MFInfo.TLabel", font=("Helvetica", 8))

        main_frame = ttk.Frame(root, padding="10 10 10 10")
        main_frame.pack(expand=True, fill=tk.BOTH)

        top_content_frame = ttk.Frame(main_frame)
        top_content_frame.pack(fill=tk.X, side=tk.TOP)

        ttk.Label(top_content_frame, text="Pengecek Kesehatan Bahan Makanan", style="Header.TLabel").pack(pady=(0,15))

        nutrition_frame = ttk.LabelFrame(top_content_frame, text="Data Nutrisi Bahan Makanan (per 100g / per saji)", padding="10")
        nutrition_frame.pack(fill=tk.X, pady=5)

        self.entries_nutrisi = {}
        # Menambahkan kembali "nama_makanan" ke dictionary nutrients_input_gui
        nutrients_input_gui = {
            "nama_makanan": ("Nama Makanan:", ""), # Input Nama Makanan ditambahkan kembali
            "kalori_bahan": ("Kalori (Kkal):", "(0-800)"),
            "protein_bahan": ("Protein (g):", "(0-50)"),
            "lemak_total_bahan": ("Lemak Total (g):", "(0-50)"),
            "karbohidrat_bahan": ("Karbohidrat (g):", "(0-100)"),
            "serat_bahan": ("Serat (g):", "(0-20.5)")
        }

        for i, (key, (label_text, range_text)) in enumerate(nutrients_input_gui.items()):
            ttk.Label(nutrition_frame, text=label_text).grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(nutrition_frame, width=25)
            entry.grid(row=i, column=1, padx=5, pady=2, sticky=tk.EW)
            self.entries_nutrisi[key] = entry
            if range_text:
                ttk.Label(nutrition_frame, text=range_text, style="RangeInfo.TLabel").grid(row=i, column=2, sticky=tk.W, padx=5)

        nutrition_frame.columnconfigure(1, weight=1)

        action_frame = ttk.Frame(top_content_frame)
        action_frame.pack(fill=tk.X, pady=5)
        self.btn_cek = ttk.Button(action_frame, text="CEK KESEHATAN BAHAN", command=self.cek_kesehatan)
        self.btn_cek.pack(side=tk.LEFT, padx=(0,10))

        result_frame = ttk.LabelFrame(top_content_frame, text="Hasil Analisis", padding="10")
        result_frame.pack(fill=tk.X, pady=5)
        ttk.Label(result_frame, text="Skor Kesehatan:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.label_hasil_skor = ttk.Label(result_frame, text="-", style="Result.TLabel", foreground="blue")
        self.label_hasil_skor.grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)
        ttk.Label(result_frame, text="Kategori:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.label_hasil_kategori = ttk.Label(result_frame, text="-", style="Result.TLabel", foreground="green")
        self.label_hasil_kategori.grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
        
        score_info_frame = ttk.LabelFrame(top_content_frame, text="Informasi Rentang Skor Kesehatan (Output)", padding="10")
        score_info_frame.pack(fill=tk.X, pady=5) 
        score_ranges = [
            ("0-20:", "Sangat Tidak Sehat", "red"), ("21-40:", "Tidak Sehat", "orange"),
            ("41-60:", "Cukup Sehat", "darkkhaki"), ("61-80:", "Sehat", "gold"),
            ("81-100:", "Sangat Sehat", "green")
        ]
        for i, (skor_range, kategori_text, color_text) in enumerate(score_ranges):
            ttk.Label(score_info_frame, text=skor_range, style="Info.TLabel", font=("Helvetica", 9, "bold")).grid(row=i, column=0, sticky=tk.W, padx=5, pady=1)
            ttk.Label(score_info_frame, text=kategori_text, style="Info.TLabel", foreground=color_text).grid(row=i, column=1, sticky=tk.W, padx=5, pady=1)
       
        
    def cek_kesehatan(self):
        print("\nVISUAL.PY: Tombol CEK KESEHATAN BAHAN ditekan.")
        # Meskipun input nama makanan ada, kita tidak perlu mengambil nilainya di sini
        # karena tidak digunakan dalam logika perhitungan.
        try:
            val_kalori = float(self.entries_nutrisi['kalori_bahan'].get() or 0)
            val_protein = float(self.entries_nutrisi['protein_bahan'].get() or 0)
            val_lemak = float(self.entries_nutrisi['lemak_total_bahan'].get() or 0)
            val_karbo = float(self.entries_nutrisi['karbohidrat_bahan'].get() or 0)
            val_serat = float(self.entries_nutrisi['serat_bahan'].get() or 0)
            print(f"VISUAL.PY: Input nutrisi dari GUI: Kalori={val_kalori}, Protein={val_protein}, Lemak={val_lemak}, Karbohidrat={val_karbo}, Serat={val_serat}")
        except ValueError:
            messagebox.showerror("Input Error", "Pastikan semua input nutrisi adalah angka yang valid! Isi dengan 0 jika tidak ada nilai.")
            print("VISUAL.PY: ValueError saat mengambil input nutrisi.")
            return
        except Exception as e:
            messagebox.showerror("Error Input Lain", f"Terjadi kesalahan saat memproses input: {str(e)}")
            print(f"VISUAL.PY: Exception {type(e).__name__} saat mengambil input nutrisi: {str(e)}")
            return

        try:
            skor, kategori, _ = hitung_skor_kesehatan(
                val_kalori, val_protein, val_lemak, val_karbo, val_serat,
            )
            print(f"VISUAL.PY: Hasil dari logic.py: Skor={skor}, Kategori='{kategori}'")

            self.label_hasil_skor.config(text=f"{skor:.2f}")
            self.label_hasil_kategori.config(text=kategori)

            color_map = {
                "Sangat Tidak Sehat": "red", "Tidak Sehat": "orange",
                "Cukup Sehat": "darkkhaki", "Sehat": "gold", "Sangat Sehat": "green",
            }
            default_color = "black"
            clean_kategori = kategori.replace(" (Pendekatan)", "") 

            if "Tidak Dapat Ditentukan" in kategori: default_color = "purple"
            elif "Tidak Terdefinisi" in kategori: default_color = "brown"
            elif "Error" in kategori: default_color = "magenta"
            
            final_color = color_map.get(clean_kategori, default_color)
            self.label_hasil_kategori.config(foreground=final_color)

        except Exception as e:
            messagebox.showerror("Fuzzy Logic or GUI Update Error", f"Gagal menghitung atau menampilkan skor: {str(e)}")
            print(f"VISUAL.PY: Exception {type(e).__name__} di blok pemanggilan utama: {str(e)}")
            traceback.print_exc()
            self.label_hasil_skor.config(text="-")
            self.label_hasil_kategori.config(text="Error Pemrosesan")
            self.label_hasil_kategori.config(foreground="black")

def start_gui():
    root = tk.Tk()
    app = IngredientCheckerApp(root)
    root.mainloop()

if __name__ == '__main__':
    print("VISUAL.PY: Menjalankan GUI secara standalone untuk testing...")
    start_gui()