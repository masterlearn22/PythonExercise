import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import traceback

# --- 1. DEKLARASI VARIABEL FUZZY ---
kalori_bahan = ctrl.Antecedent(np.arange(0, 801, 1), 'kalori_bahan')
protein_bahan = ctrl.Antecedent(np.arange(0, 51, 1), 'protein_bahan')
lemak_total_bahan = ctrl.Antecedent(np.arange(0, 51, 1), 'lemak_total_bahan')
karbohidrat_bahan = ctrl.Antecedent(np.arange(0, 101, 1), 'karbohidrat_bahan')
serat_bahan = ctrl.Antecedent(np.arange(0, 21, 0.5), 'serat_bahan')
kesehatan_bahan = ctrl.Consequent(np.arange(0, 101, 1), 'kesehatan_bahan', defuzzify_method='centroid')

# --- 2. PEMBUATAN FUNGSI KEANGGOTAAN (MEMBERSHIP FUNCTIONS) ---
# Kalori (5 set)
kalori_bahan['sangat_rendah'] = fuzz.trimf(kalori_bahan.universe, [0, 75, 150])
kalori_bahan['rendah'] = fuzz.trimf(kalori_bahan.universe, [100, 200, 300])
kalori_bahan['sedang'] = fuzz.trimf(kalori_bahan.universe, [250, 375, 500])
kalori_bahan['tinggi'] = fuzz.trimf(kalori_bahan.universe, [450, 575, 700])
kalori_bahan['sangat_tinggi'] = fuzz.trapmf(kalori_bahan.universe, [650, 725, 800, 800])

# Protein (5 set)
protein_bahan['sangat_rendah'] = fuzz.trapmf(protein_bahan.universe, [0, 0, 2, 5])
protein_bahan['rendah'] = fuzz.trimf(protein_bahan.universe, [3, 8, 12])
protein_bahan['cukup'] = fuzz.trimf(protein_bahan.universe, [10, 18, 26])
protein_bahan['tinggi'] = fuzz.trimf(protein_bahan.universe, [22, 30, 38])
protein_bahan['sangat_tinggi'] = fuzz.trapmf(protein_bahan.universe, [35, 42, 50, 50])

# Lemak (5 set)
lemak_total_bahan['sangat_rendah'] = fuzz.trapmf(lemak_total_bahan.universe, [0, 0, 2, 5])
lemak_total_bahan['rendah'] = fuzz.trimf(lemak_total_bahan.universe, [3, 8, 13])
lemak_total_bahan['sedang'] = fuzz.trimf(lemak_total_bahan.universe, [10, 18, 26])
lemak_total_bahan['tinggi'] = fuzz.trimf(lemak_total_bahan.universe, [22, 30, 38])
lemak_total_bahan['sangat_tinggi'] = fuzz.trapmf(lemak_total_bahan.universe, [35, 42, 50, 50])

# Karbohidrat (4 set)
karbohidrat_bahan['sangat_rendah'] = fuzz.trapmf(karbohidrat_bahan.universe, [0, 0, 10, 20])
karbohidrat_bahan['rendah'] = fuzz.trimf(karbohidrat_bahan.universe, [15, 30, 45])
karbohidrat_bahan['sedang'] = fuzz.trimf(karbohidrat_bahan.universe, [40, 55, 70])
karbohidrat_bahan['tinggi'] = fuzz.trapmf(karbohidrat_bahan.universe, [65, 80, 100, 100])

# Serat (4 set)
serat_bahan['sangat_rendah'] = fuzz.trapmf(serat_bahan.universe, [0, 0, 1, 2.5])
serat_bahan['rendah'] = fuzz.trimf(serat_bahan.universe, [1.5, 3.5, 6])
serat_bahan['cukup'] = fuzz.trimf(serat_bahan.universe, [5, 8, 11])
serat_bahan['tinggi'] = fuzz.trapmf(serat_bahan.universe, [9, 13, 20, 20])

# Output Kesehatan
kesehatan_bahan['sangat_tidak_sehat'] = fuzz.trimf(kesehatan_bahan.universe, [0, 10, 20])
kesehatan_bahan['tidak_sehat'] = fuzz.trimf(kesehatan_bahan.universe, [15, 30, 45])
kesehatan_bahan['cukup_sehat'] = fuzz.trimf(kesehatan_bahan.universe, [40, 55, 70])
kesehatan_bahan['sehat'] = fuzz.trimf(kesehatan_bahan.universe, [65, 80, 90])
kesehatan_bahan['sangat_sehat'] = fuzz.trimf(kesehatan_bahan.universe, [85, 95, 100])

# Target: Sangat Tidak Sehat - Kondisi paling buruk.
rule1 = ctrl.Rule(kalori_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_tinggi'] & protein_bahan['sangat_rendah'] & serat_bahan['sangat_rendah'], kesehatan_bahan['sangat_tidak_sehat'])
# Target: Sangat Tidak Sehat - Kalori tinggi, lemak sangat tinggi, karbohidrat tinggi (maks).
rule2 = ctrl.Rule(kalori_bahan['tinggi'] & lemak_total_bahan['sangat_tinggi'] & karbohidrat_bahan['tinggi'], kesehatan_bahan['sangat_tidak_sehat'])
# Target: Tidak Sehat - Kalori tinggi, lemak/karbo tinggi, protein rendah.
rule3 = ctrl.Rule(kalori_bahan['tinggi'] & (lemak_total_bahan['tinggi'] | karbohidrat_bahan['tinggi']) & protein_bahan['rendah'], kesehatan_bahan['tidak_sehat'])
# Target: Tidak Sehat - Lemak sangat tinggi, serat sangat rendah, protein rendah/sangat_rendah, & kalori tidak sangat tinggi.
rule4 = ctrl.Rule(lemak_total_bahan['sangat_tinggi'] & serat_bahan['sangat_rendah'] & (protein_bahan['sangat_rendah'] | protein_bahan['rendah']) & ~kalori_bahan['sangat_tinggi'], kesehatan_bahan['tidak_sehat'])
# Target: Tidak Sehat - Protein sangat rendah, tetapi kalori tidak sangat rendah.
rule5 = ctrl.Rule(protein_bahan['sangat_rendah'] & ~kalori_bahan['sangat_rendah'] & ~kalori_bahan['rendah'] & ~kalori_bahan['sangat_tinggi'], kesehatan_bahan['tidak_sehat'])
# Target: Cukup Sehat - Profil serba sedang/cukup, serat cukup/rendah.
rule6 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['cukup'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & (serat_bahan['cukup'] | serat_bahan['rendah']), kesehatan_bahan['cukup_sehat'])
# Target: Cukup Sehat - Protein tinggi, namun lemak, kalori, serat hanya cukup/sedang.
rule7 = ctrl.Rule(protein_bahan['tinggi'] & lemak_total_bahan['sedang'] & kalori_bahan['sedang'] & serat_bahan['cukup'], kesehatan_bahan['cukup_sehat'])
# Target: Cukup Sehat - Serat cukup, kalori sedang, dan lemak tidak tinggi/sangat tinggi.
rule8 = ctrl.Rule(serat_bahan['cukup'] & kalori_bahan['sedang'] & ~(lemak_total_bahan['tinggi'] | lemak_total_bahan['sangat_tinggi']), kesehatan_bahan['cukup_sehat'])
# Target: Sehat - Protein tinggi, lemak rendah, kalori sedang/rendah, serat cukup.
rule9 = ctrl.Rule(protein_bahan['tinggi'] & (lemak_total_bahan['rendah'] | lemak_total_bahan['sangat_rendah']) & (kalori_bahan['sedang'] | kalori_bahan['rendah']) & serat_bahan['cukup'], kesehatan_bahan['sehat'])
# Target: Sehat - Profil rendah kalori, lemak, karbo; dengan protein cukup dan serat tinggi (maks).
rule10 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['cukup'] & (lemak_total_bahan['rendah'] | lemak_total_bahan['sangat_rendah']) & (karbohidrat_bahan['rendah'] | karbohidrat_bahan['sangat_rendah']) & serat_bahan['tinggi'], kesehatan_bahan['sehat'])
# Target: Sangat Sehat - Protein tinggi/sangat tinggi, lemak sangat rendah, karbo dan kalori rendah.
rule11 = ctrl.Rule((protein_bahan['tinggi'] | protein_bahan['sangat_tinggi']) & lemak_total_bahan['sangat_rendah'] & (karbohidrat_bahan['rendah'] | karbohidrat_bahan['sangat_rendah']) & (kalori_bahan['rendah'] | kalori_bahan['sangat_rendah']), kesehatan_bahan['sangat_sehat'])
# Target: Sangat Sehat - Profil ideal; protein sangat tinggi, lemak sangat rendah, kalori rendah, karbo sangat rendah, serat tinggi (maks).
rule12 = ctrl.Rule(protein_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_rendah'] & (kalori_bahan['rendah'] | kalori_bahan['sangat_rendah']) & karbohidrat_bahan['sangat_rendah'] & serat_bahan['tinggi'], kesehatan_bahan['sangat_sehat'])
# Target: Sangat Sehat - Kalori sangat rendah, protein tinggi, lemak sangat rendah, serat dan karbo baik.
rule13 = ctrl.Rule(kalori_bahan['sangat_rendah'] & (protein_bahan['tinggi'] | protein_bahan['sangat_tinggi']) & lemak_total_bahan['sangat_rendah'] & (serat_bahan['tinggi'] | serat_bahan['cukup']) & (karbohidrat_bahan['sangat_rendah'] | karbohidrat_bahan['rendah']), kesehatan_bahan['sangat_sehat'])

# Adaptasi aturan 14-51 ke MF 4-set untuk Karbo & Serat
# Target: Sehat - K_R, P_C/T, L_S, Kr_R, S_Tinggi (maks).
rule14 = ctrl.Rule(kalori_bahan['rendah'] & (protein_bahan['cukup'] | protein_bahan['tinggi']) & lemak_total_bahan['sedang'] & karbohidrat_bahan['rendah'] & serat_bahan['tinggi'], kesehatan_bahan['sehat'])
# Target: Sehat - K_S, L_S, Kr_S; P_ST, S_Tinggi (maks).
rule15 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['sangat_tinggi'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & serat_bahan['tinggi'], kesehatan_bahan['sehat'])
# Target: Cukup Sehat - K_S, P_T, S_Tinggi, Kr_R, TAPI L_T.
rule16 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['tinggi'] & lemak_total_bahan['tinggi'] & karbohidrat_bahan['rendah'] & serat_bahan['tinggi'], kesehatan_bahan['cukup_sehat'])
# Target: Tidak Sehat - Serba sedang, TAPI P_R, S_R. (Ini kasus input kosong yang jadi 0 semua sebelumnya)
rule17 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['rendah'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & serat_bahan['rendah'], kesehatan_bahan['tidak_sehat'])
# Target: Tidak Sehat - Semua nutrisi sangat rendah.
rule18 = ctrl.Rule(kalori_bahan['sangat_rendah'] & protein_bahan['sangat_rendah'] & lemak_total_bahan['sangat_rendah'] & karbohidrat_bahan['sangat_rendah'] & serat_bahan['sangat_rendah'], kesehatan_bahan['tidak_sehat'])
# Target: Tidak Sehat - K_T, Kr_T; meskipun P_C, L_S, S_Cukup.
rule19 = ctrl.Rule(kalori_bahan['tinggi'] & protein_bahan['cukup'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['tinggi'] & serat_bahan['cukup'], kesehatan_bahan['tidak_sehat'])
# Target: Sangat Sehat - K_S, Kr_S; P_ST, S_Tinggi (maks), L_R.
rule20 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['sangat_tinggi'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['sedang'] & serat_bahan['tinggi'], kesehatan_bahan['sangat_sehat'])
# Target: Cukup Sehat - Nutrisi lain sempurna, TAPI K_ST.
rule21 = ctrl.Rule(kalori_bahan['sangat_tinggi'] & protein_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_rendah'] & karbohidrat_bahan['sangat_rendah'] & serat_bahan['tinggi'], kesehatan_bahan['cukup_sehat'])
# Target: Cukup Sehat - K_R, P_C, L_S, Kr_R, S_Cukup.
rule22 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['cukup'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['rendah'] & serat_bahan['cukup'], kesehatan_bahan['cukup_sehat'])
# Target: Sehat - K_R, P_T, L_S, Kr_R, S_Tinggi.
rule23 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['tinggi'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['rendah'] & serat_bahan['tinggi'], kesehatan_bahan['sehat'])
# Target: Tidak Sehat - L_ST, meskipun P dan S baik (cukup/tinggi). (Karbohidrat tidak dianggap di aturan ini).
rule24 = ctrl.Rule(lemak_total_bahan['sangat_tinggi'] & (protein_bahan['cukup'] | protein_bahan['tinggi'] | protein_bahan['sangat_tinggi']) & (serat_bahan['cukup'] | serat_bahan['tinggi']), kesehatan_bahan['tidak_sehat'])

# Target: Sehat - K_S, P_T, L_S, Kr_R, S_Tinggi
rule25 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['tinggi'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['rendah'] & serat_bahan['tinggi'], kesehatan_bahan['sehat'])
# Target: Sehat - K_R, P_C, L_R, Kr_S, S_Cukup
rule26 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['cukup'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['sedang'] & serat_bahan['cukup'], kesehatan_bahan['sehat'])
# Target: Tidak Sehat - K_T, P_T, L_S, Kr_T, S_Cukup
rule27 = ctrl.Rule(kalori_bahan['tinggi'] & protein_bahan['tinggi'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['tinggi'] & serat_bahan['cukup'], kesehatan_bahan['tidak_sehat'])
# Target: Cukup Sehat - K_S, P_C, Kr_S, S_Cukup, TAPI L_T
rule28 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['cukup'] & lemak_total_bahan['tinggi'] & karbohidrat_bahan['sedang'] & serat_bahan['cukup'], kesehatan_bahan['cukup_sehat'])
# Target: Sangat Tidak Sehat - K_ST, L_ST, P_C/T, Kr_S, S_Cukup/Tinggi
rule29 = ctrl.Rule(kalori_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_tinggi'] & (protein_bahan['cukup'] | protein_bahan['tinggi']) & karbohidrat_bahan['sedang'] & (serat_bahan['cukup'] | serat_bahan['tinggi']), kesehatan_bahan['sangat_tidak_sehat'])
# Target: Sangat Sehat - K_S, P_T, L_SR, Kr_SR, S_Tinggi
rule30 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['tinggi'] & lemak_total_bahan['sangat_rendah'] & karbohidrat_bahan['sangat_rendah'] & serat_bahan['tinggi'], kesehatan_bahan['sangat_sehat'])
# Target: Sangat Tidak Sehat - K_T, P_SR, L_T, Kr_T, S_SR
rule31 = ctrl.Rule(kalori_bahan['tinggi'] & protein_bahan['sangat_rendah'] & lemak_total_bahan['tinggi'] & karbohidrat_bahan['tinggi'] & serat_bahan['sangat_rendah'], kesehatan_bahan['sangat_tidak_sehat'])
# Target: Cukup Sehat - K_R, P_T, L_R, S_Cukup, TAPI Kr_T
rule32 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['tinggi'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['tinggi'] & serat_bahan['cukup'], kesehatan_bahan['cukup_sehat'])
# Target: Sehat - K_S, P_C, L_S, Kr_SR, S_Tinggi
rule33 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['cukup'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sangat_rendah'] & serat_bahan['tinggi'], kesehatan_bahan['sehat'])
# Target: Cukup Sehat - K_S, P_R, L_R, Kr_R, S_R
rule34 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['rendah'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['rendah'] & serat_bahan['rendah'], kesehatan_bahan['cukup_sehat'])
# Target: Tidak Sehat - K_T, P_ST, L_ST, Kr_T (maks), S_Tinggi (maks) -> Karbohidrat tinggi (maks) bukan sangat_tinggi
rule35 = ctrl.Rule(kalori_bahan['tinggi'] & protein_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_tinggi'] & karbohidrat_bahan['tinggi'] & serat_bahan['tinggi'], kesehatan_bahan['tidak_sehat'])
# Target: Sehat - K_R, P_ST, L_S, Kr_S, S_Tinggi
rule36 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['sangat_tinggi'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & serat_bahan['tinggi'], kesehatan_bahan['sehat'])
# Target: Cukup Sehat - K_R, P_R, L_R, Kr_R, S_Tinggi
rule37 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['rendah'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['rendah'] & serat_bahan['tinggi'], kesehatan_bahan['cukup_sehat'])
# Target: Cukup Sehat - K_R, P_C, L_T, Kr_S, S_Cukup
rule38 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['cukup'] & lemak_total_bahan['tinggi'] & karbohidrat_bahan['sedang'] & serat_bahan['cukup'], kesehatan_bahan['cukup_sehat'])
# Target: Tidak Sehat - K_S, P_T, L_T, Kr_T, S_R
rule39 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['tinggi'] & lemak_total_bahan['tinggi'] & karbohidrat_bahan['tinggi'] & serat_bahan['rendah'], kesehatan_bahan['tidak_sehat'])
# Target: Tidak Sehat - K_S, P_SR, L_S, Kr_S, S_Cukup
rule40 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['sangat_rendah'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & serat_bahan['cukup'], kesehatan_bahan['tidak_sehat'])
# Target: Cukup Sehat - K_T, TAPI P_T, L_R, Kr_R, S_Tinggi
rule41 = ctrl.Rule(kalori_bahan['tinggi'] & protein_bahan['tinggi'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['rendah'] & serat_bahan['tinggi'], kesehatan_bahan['cukup_sehat'])
# Target: Tidak Sehat - K_T, P_C, L_S, Kr_S, S_R
rule42 = ctrl.Rule(kalori_bahan['tinggi'] & protein_bahan['cukup'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & serat_bahan['rendah'], kesehatan_bahan['tidak_sehat'])
# Target: Cukup Sehat - L_T, TAPI K_R, P_T, Kr_SR, S_Tinggi
rule43 = ctrl.Rule(lemak_total_bahan['tinggi'] & kalori_bahan['rendah'] & protein_bahan['tinggi'] & karbohidrat_bahan['sangat_rendah'] & serat_bahan['tinggi'], kesehatan_bahan['cukup_sehat'])
# Target: Sangat Tidak Sehat - L_ST, K_S, P_R, Kr_S, S_R
rule44 = ctrl.Rule(lemak_total_bahan['sangat_tinggi'] & kalori_bahan['sedang'] & protein_bahan['rendah'] & karbohidrat_bahan['sedang'] & serat_bahan['rendah'], kesehatan_bahan['sangat_tidak_sehat'])
# Target: Cukup Sehat - Kr_T, TAPI K_R, P_T, L_R, S_Tinggi
rule45 = ctrl.Rule(karbohidrat_bahan['tinggi'] & kalori_bahan['rendah'] & protein_bahan['tinggi'] & lemak_total_bahan['rendah'] & serat_bahan['tinggi'], kesehatan_bahan['cukup_sehat'])
# Target: Sangat Tidak Sehat - Kr_T (maks), K_S, P_R, L_S, S_R (Karbohidrat tinggi menjadi sangat tinggi di MF 4 set)
rule46 = ctrl.Rule(karbohidrat_bahan['tinggi'] & kalori_bahan['sedang'] & protein_bahan['rendah'] & lemak_total_bahan['sedang'] & serat_bahan['rendah'], kesehatan_bahan['sangat_tidak_sehat'])
# Target: Sangat Sehat - Hampir sempurna, tapi serat hanya cukup.
rule47 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_rendah'] & karbohidrat_bahan['sangat_rendah'] & serat_bahan['cukup'], kesehatan_bahan['sangat_sehat'])
# Target: Cukup Sehat - K_S, P_C, L_R, Kr_S, TAPI S_R.
rule48 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['cukup'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['sedang'] & serat_bahan['rendah'], kesehatan_bahan['cukup_sehat'])
# Target: Cukup Sehat - K_R, P_R, L_S, Kr_S, S_Cukup.
rule49 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['rendah'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & serat_bahan['cukup'], kesehatan_bahan['cukup_sehat'])
# Target: Sehat - K_SR, P_C, L_R, Kr_R, S_Cukup.
rule50 = ctrl.Rule(kalori_bahan['sangat_rendah'] & protein_bahan['cukup'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['rendah'] & serat_bahan['cukup'], kesehatan_bahan['sehat'])
# Target: Sangat Tidak Sehat - K_ST, L_ST, Kr_T (maks). (Ini adalah rule51 yang disesuaikan)
rule51 = ctrl.Rule(kalori_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_tinggi'] & karbohidrat_bahan['tinggi'], kesehatan_bahan['sangat_tidak_sehat'])

all_rules = [
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
    rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
    rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28,
    rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37,
    rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46,
    rule47, rule48, rule49, rule50, rule51
]

# --- 4. PEMBUATAN CONTROL SYSTEM ---
try:
    penilaian_ctrl_system = ctrl.ControlSystem(all_rules)
except Exception as e:
    print(f"LOGIC.PY: ERROR saat membuat ControlSystem: {e}")
    traceback.print_exc()
    penilaian_ctrl_system = None

# --- 5. FUNGSI UTAMA UNTUK MENGHITUNG ---
def hitung_skor_kesehatan(val_kalori, val_protein, val_lemak, val_karbo, val_serat, show_plot=False):
    if penilaian_ctrl_system is None:
        print("LOGIC.PY: ControlSystem tidak terinisialisasi dengan benar.")
        return 0.0, "Error Sistem Fuzzy (Inisialisasi Gagal)", None

    try:
        penilaian_simulasi = ctrl.ControlSystemSimulation(penilaian_ctrl_system)
    except Exception as e_sim:
        print(f"LOGIC.PY: ERROR saat membuat ControlSystemSimulation: {e_sim}")
        traceback.print_exc()
        return 0.0, "Error Sistem Fuzzy (Simulasi Gagal)", None

    skor_hasil_default = 0.0
    kategori_label_default = "Tidak Dapat Ditentukan (Cakupan Aturan Kurang)"
    simulasi_untuk_plot = None
    skor_hasil_final = skor_hasil_default
    kategori_label_final = kategori_label_default

    try:
        print("\nLOGIC.PY: Mencoba mengatur input...")
        penilaian_simulasi.input['kalori_bahan'] = val_kalori
        penilaian_simulasi.input['protein_bahan'] = val_protein
        penilaian_simulasi.input['lemak_total_bahan'] = val_lemak
        penilaian_simulasi.input['karbohidrat_bahan'] = val_karbo
        penilaian_simulasi.input['serat_bahan'] = val_serat
        print(f"LOGIC.PY: Input diatur. Kalori: {val_kalori}, Protein: {val_protein}, Lemak: {val_lemak}, Karbo: {val_karbo}, Serat: {val_serat}")

        print("LOGIC.PY: Mencoba melakukan komputasi fuzzy...")
        penilaian_simulasi.compute()
        print("LOGIC.PY: Komputasi fuzzy selesai.")

        output_kesehatan = penilaian_simulasi.output.get('kesehatan_bahan')

        if output_kesehatan is not None and not np.isnan(output_kesehatan):
            print(f"LOGIC.PY: Output normal ditemukan. Skor mentah: {output_kesehatan}")
            skor_hasil = output_kesehatan
            simulasi_untuk_plot = penilaian_simulasi

            if skor_hasil <= 20: kategori_label_final = "Sangat Tidak Sehat"
            elif skor_hasil <= 45: kategori_label_final = "Tidak Sehat"
            elif skor_hasil <= 70: kategori_label_final = "Cukup Sehat"
            elif skor_hasil <= 90: kategori_label_final = "Sehat"
            else: kategori_label_final = "Sangat Sehat"
            skor_hasil_final = skor_hasil
        else:
            print(f"LOGIC.PY: Kunci 'kesehatan_bahan' TIDAK DITEMUKAN atau None. Menggunakan kategori default.")

        if show_plot and simulasi_untuk_plot is not None:
            print("LOGIC.PY: Menyiapkan plot...")
            try:
                plt.figure(f"Plot Fuzzy: K{val_kalori},P{val_protein},L{val_lemak},K{val_karbo},S{val_serat}")
                kesehatan_bahan.view(sim=simulasi_untuk_plot)
                plt.title("Proses Inferensi Fuzzy Mamdani untuk Kesehatan Bahan")
                print("LOGIC.PY: Plot disiapkan.")
                if plt.get_fignums():
                    plt.show(block=False)
                    plt.pause(0.1)
            except Exception as e_plot_view:
                print(f"LOGIC.PY: Gagal saat menyiapkan view plot: {e_plot_view}")
                traceback.print_exc()
        elif show_plot and simulasi_untuk_plot is None:
            print("LOGIC.PY: Tidak dapat menampilkan plot karena hasil simulasi tidak valid (simulasi_untuk_plot is None).")

        return skor_hasil_final, kategori_label_final, simulasi_untuk_plot

    except Exception as e:
        print(f"LOGIC.PY: Terjadi ERROR selama komputasi fuzzy atau plotting: {type(e).__name__} - {e}")
        traceback.print_exc()
        return skor_hasil_default, "Error Internal Sistem (Periksa Konsol)", None