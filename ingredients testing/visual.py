import tkinter as tk
from tkinter import ttk, messagebox
from logic import hitung_skor_kesehatan # Impor fungsi dari logic.py
import traceback # Untuk traceback error yang lebih detail

class IngredientCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pengecek Ingredient Nutrisi (Fuzzy Mamdani)")
        self.root.geometry("550x780") # Ukuran window diperbesar untuk informasi tambahan

        # Style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", font=("Helvetica", 10))
        style.configure("TButton", font=("Helvetica", 10, "bold"), padding=5)
        style.configure("TEntry", font=("Helvetica", 10), padding=5)
        style.configure("Header.TLabel", font=("Helvetica", 14, "bold"))
        style.configure("Result.TLabel", font=("Helvetica", 12, "bold"))
        style.configure("Info.TLabel", font=("Helvetica", 9)) # Style untuk label informasi skor

        main_frame = ttk.Frame(root, padding="10 10 10 10")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # --- Judul ---
        ttk.Label(main_frame, text="Pengecek Kesehatan Bahan Makanan", style="Header.TLabel").pack(pady=(0,15))

        # --- Input Data Pengguna (untuk masa depan) ---
        user_frame = ttk.LabelFrame(main_frame, text="Data Pengguna (Wanita 19-29 Thn)", padding="10 10 10 10")
        user_frame.pack(fill=tk.X, pady=5)

        ttk.Label(user_frame, text="Berat Badan (kg):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.entry_berat = ttk.Entry(user_frame, width=15)
        self.entry_berat.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(user_frame, text="Tinggi Badan (cm):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.entry_tinggi = ttk.Entry(user_frame, width=15)
        self.entry_tinggi.grid(row=1, column=1, padx=5, pady=2)
        ttk.Label(user_frame, text="*Saat ini belum mempengaruhi logika").grid(row=0, column=2, rowspan=2, sticky=tk.W, padx=10)


        # --- Input Data Nutrisi Bahan Makanan ---
        nutrition_frame = ttk.LabelFrame(main_frame, text="Data Nutrisi Bahan Makanan (per 100g / per saji)", padding="10 10 10 10")
        nutrition_frame.pack(fill=tk.X, pady=5)

        self.entries_nutrisi = {}
        nutrients = {
            "nama_bahan": "Nama Bahan:",
            "kalori_bahan": "Kalori (Kkal):",
            "protein_bahan": "Protein (g):",
            "lemak_total_bahan": "Lemak Total (g):",
            "karbohidrat_bahan": "Karbohidrat (g):",
            "serat_bahan": "Serat (g):"
        }

        for i, (key, label_text) in enumerate(nutrients.items()):
            ttk.Label(nutrition_frame, text=label_text).grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(nutrition_frame, width=30)
            entry.grid(row=i, column=1, padx=5, pady=2, sticky=tk.EW)
            self.entries_nutrisi[key] = entry

        nutrition_frame.columnconfigure(1, weight=1)

        # --- Tombol Aksi ---
        action_frame = ttk.Frame(main_frame, padding="10 0 0 0")
        action_frame.pack(fill=tk.X, pady=5)

        self.btn_cek = ttk.Button(action_frame, text="CEK KESEHATAN BAHAN", command=self.cek_kesehatan)
        self.btn_cek.pack(side=tk.LEFT, padx=(0,10))

        self.check_show_plot_var = tk.BooleanVar(value=False)
        self.check_show_plot = ttk.Checkbutton(action_frame, text="Tampilkan Plot Fuzzy", variable=self.check_show_plot_var)
        self.check_show_plot.pack(side=tk.LEFT)


        # --- Hasil Analisis ---
        result_frame = ttk.LabelFrame(main_frame, text="Hasil Analisis", padding="10 10 10 10")
        result_frame.pack(fill=tk.X, pady=5)

        ttk.Label(result_frame, text="Skor Kesehatan:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.label_hasil_skor = ttk.Label(result_frame, text="-", style="Result.TLabel", foreground="blue")
        self.label_hasil_skor.grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)

        ttk.Label(result_frame, text="Kategori:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.label_hasil_kategori = ttk.Label(result_frame, text="-", style="Result.TLabel", foreground="green")
        self.label_hasil_kategori.grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)

        # --- Informasi Rentang Skor Kesehatan ---
        score_info_frame = ttk.LabelFrame(main_frame, text="Informasi Rentang Skor Kesehatan", padding="10 10 10 10")
        score_info_frame.pack(fill=tk.X, pady=10)

        score_ranges = [
            ("0-20:", "Sangat Tidak Sehat", "red"),
            ("21-40:", "Tidak Sehat", "orange"),
            ("41-60:", "Cukup Sehat", "darkkhaki"),
            ("61-80:", "Sehat", "gold"),
            ("81-100:", "Sangat Sehat", "green")
        ]

        for i, (skor_range, kategori_text, color_text) in enumerate(score_ranges):
            ttk.Label(score_info_frame, text=skor_range, style="Info.TLabel", font=("Helvetica", 9, "bold")).grid(row=i, column=0, sticky=tk.W, padx=5, pady=1)
            ttk.Label(score_info_frame, text=kategori_text, style="Info.TLabel", foreground=color_text).grid(row=i, column=1, sticky=tk.W, padx=5, pady=1)


    def cek_kesehatan(self):
        print("\nVISUAL.PY: Tombol CEK KESEHATAN BAHAN ditekan.")
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
            show_plot_flag = self.check_show_plot_var.get()
            print(f"VISUAL.PY: Memanggil hitung_skor_kesehatan dengan show_plot={show_plot_flag}")
            
            skor, kategori, sim_obj = hitung_skor_kesehatan( # Tangkap objek simulasi
                val_kalori, val_protein, val_lemak, val_karbo, val_serat,
                show_plot=show_plot_flag # show_plot di logic akan menangani tampilan plot jika True
            )
            print(f"VISUAL.PY: Hasil dari logic.py: Skor={skor}, Kategori='{kategori}'")

            self.label_hasil_skor.config(text=f"{skor:.2f}")
            self.label_hasil_kategori.config(text=kategori)

            # Atur warna kategori
            if kategori == "Sangat Tidak Sehat": self.label_hasil_kategori.config(foreground="red")
            elif kategori == "Tidak Sehat": self.label_hasil_kategori.config(foreground="orange")
            elif kategori == "Cukup Sehat": self.label_hasil_kategori.config(foreground="darkkhaki")
            elif kategori == "Sehat": self.label_hasil_kategori.config(foreground="gold")
            elif kategori == "Sangat Sehat": self.label_hasil_kategori.config(foreground="green")
            elif "Tidak Dapat Ditentukan" in kategori: self.label_hasil_kategori.config(foreground="purple")
            elif "Tidak Terdefinisi" in kategori: self.label_hasil_kategori.config(foreground="brown")
            elif "Error" in kategori: self.label_hasil_kategori.config(foreground="magenta")
            else: self.label_hasil_kategori.config(foreground="black")

            # Jika user mencentang "Tampilkan Plot Fuzzy" dan simulasi berhasil
            if show_plot_flag and sim_obj and \
               kategori not in ["Tidak Dapat Ditentukan (Cakupan Aturan Kurang)",
                                "Tidak Terdefinisi (Input Ambigu/Aktivasi Rendah)"] and \
               not kategori.startswith("Error"):
                try:
                    plt.figure(f"Plot Fuzzy GUI: K{val_kalori},P{val_protein},L{val_lemak}") # Judul unik
                    kesehatan_bahan.view(sim=sim_obj) # kesehatan_bahan adalah variabel global dari logic.py
                                                      # Seharusnya ini diimpor atau diakses dengan cara lain jika logic.py tidak dieksekusi sepenuhnya
                                                      # Namun, untuk skfuzzy, objek Antecedent/Consequent (seperti kesehatan_bahan)
                                                      # yang digunakan untuk .view() adalah bagian dari sistem kontrol yang sudah ada.
                                                      # Jika hitung_skor_kesehatan mengembalikan objek Consequent yang relevan, itu lebih baik.
                                                      # Untuk sekarang, kita asumsikan kesehatan_bahan dari logic.py bisa diakses jika plot logic jalan.
                                                      # Cara yang lebih aman: `logic.kesehatan_bahan.view(sim=sim_obj)` jika logic.py punya kesehatan_bahan sebagai atribut global
                                                      # Atau, idealnya, hitung_skor_kesehatan juga mengembalikan objek Consequent yang tepat.
                                                      # Berhubung `kesehatan_bahan.view` dipanggil di logic.py jika plotnya dari sana,
                                                      # pemanggilan plot dari GUI bisa jadi redundan atau butuh penanganan lebih lanjut.
                                                      # Untuk sementara, jika show_plot=True di logic.py sudah menampilkan plot,
                                                      # mungkin tidak perlu menampilkannya lagi dari GUI secara terpisah, kecuali desainnya memang begitu.
                                                      # Kode `hitung_skor_kesehatan` sudah menghandle plot jika `show_plot=True`.
                    # plt.show(block=False) # logic.py sudah menghandle ini.
                    print("VISUAL.PY: Plot dari logic.py seharusnya sudah muncul jika diaktifkan di sana.")
                except Exception as e_gui_plot:
                    print(f"VISUAL.PY: Gagal menampilkan plot dari GUI: {e_gui_plot}")
                    messagebox.showwarning("Plot Error", f"Gagal menampilkan plot dari GUI: {e_gui_plot}")


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