import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import traceback # Untuk traceback error yang lebih detail

# --- 1. DEKLARASI VARIABEL FUZZY ---
kalori_bahan = ctrl.Antecedent(np.arange(0, 801, 1), 'kalori_bahan')
protein_bahan = ctrl.Antecedent(np.arange(0, 51, 1), 'protein_bahan')
lemak_total_bahan = ctrl.Antecedent(np.arange(0, 51, 1), 'lemak_total_bahan')
karbohidrat_bahan = ctrl.Antecedent(np.arange(0, 101, 1), 'karbohidrat_bahan')
serat_bahan = ctrl.Antecedent(np.arange(0, 21, 0.5), 'serat_bahan')
kesehatan_bahan = ctrl.Consequent(np.arange(0, 101, 1), 'kesehatan_bahan', defuzzify_method='centroid')

# --- 2. PEMBUATAN FUNGSI KEANGGOTAAN (MEMBERSHIP FUNCTIONS) DENGAN KOMENTAR RENTANG ---

# Kalori (Universe 0-800)
kalori_bahan['sangat_rendah'] = fuzz.trapmf(kalori_bahan.universe, [0, 0, 75, 225])        # Rentang input efektif: 0 - 225
kalori_bahan['rendah'] = fuzz.trimf(kalori_bahan.universe, [75, 225, 400])                  # Rentang input efektif: 75 - 400
kalori_bahan['sedang'] = fuzz.trimf(kalori_bahan.universe, [225, 400, 600])                # Rentang input efektif: 225 - 600
kalori_bahan['tinggi'] = fuzz.trimf(kalori_bahan.universe, [400, 600, 750])                # Rentang input efektif: 400 - 750
kalori_bahan['sangat_tinggi'] = fuzz.trapmf(kalori_bahan.universe, [600, 750, 800, 800])  # Rentang input efektif: 600 - 800

# Protein (Universe 0-50)
# Puncak referensi: p_sr=5, p_r=12.5, p_c=25, p_t=37.5, p_st=45
protein_bahan['sangat_rendah'] = fuzz.trapmf(protein_bahan.universe, [0, 0, 5, 12.5])       # Rentang input efektif: 0 - 12.5
protein_bahan['rendah'] = fuzz.trimf(protein_bahan.universe, [5, 12.5, 25])                 # Rentang input efektif: 5 - 25
protein_bahan['cukup'] = fuzz.trimf(protein_bahan.universe, [12.5, 25, 37.5])               # Rentang input efektif: 12.5 - 37.5
protein_bahan['tinggi'] = fuzz.trimf(protein_bahan.universe, [25, 37.5, 45])                # Rentang input efektif: 25 - 45
protein_bahan['sangat_tinggi'] = fuzz.trapmf(protein_bahan.universe, [37.5, 45, 50, 50])   # Rentang input efektif: 37.5 - 50

# Lemak (Universe 0-50)
# Puncak referensi: p_sr=5, p_r=12.5, p_s=25, p_t=37.5, p_st=45
lemak_total_bahan['sangat_rendah'] = fuzz.trapmf(lemak_total_bahan.universe, [0, 0, 5, 12.5])    # Rentang input efektif: 0 - 12.5
lemak_total_bahan['rendah'] = fuzz.trimf(lemak_total_bahan.universe, [5, 12.5, 25])              # Rentang input efektif: 5 - 25
lemak_total_bahan['sedang'] = fuzz.trimf(lemak_total_bahan.universe, [12.5, 25, 37.5])            # Rentang input efektif: 12.5 - 37.5
lemak_total_bahan['tinggi'] = fuzz.trimf(lemak_total_bahan.universe, [25, 37.5, 45])             # Rentang input efektif: 25 - 45
lemak_total_bahan['sangat_tinggi'] = fuzz.trapmf(lemak_total_bahan.universe, [37.5, 45, 50, 50])# Rentang input efektif: 37.5 - 50

# Karbohidrat (Universe 0-100)
# Puncak referensi: p_sr=5, p_r=25, p_s=50, p_t=75, p_st=90 (disesuaikan dari sebelumnya)
karbohidrat_bahan['sangat_rendah'] = fuzz.trapmf(karbohidrat_bahan.universe, [0, 0, 5, 25])     # Rentang input efektif: 0 - 25
karbohidrat_bahan['rendah'] = fuzz.trimf(karbohidrat_bahan.universe, [5, 25, 50])               # Rentang input efektif: 5 - 50
karbohidrat_bahan['sedang'] = fuzz.trimf(karbohidrat_bahan.universe, [25, 50, 75])              # Rentang input efektif: 25 - 75
karbohidrat_bahan['tinggi'] = fuzz.trimf(karbohidrat_bahan.universe, [50, 75, 90])              # Rentang input efektif: 50 - 90
karbohidrat_bahan['sangat_tinggi'] = fuzz.trapmf(karbohidrat_bahan.universe, [75, 90, 100, 100])# Rentang input efektif: 75 - 100

# Serat (Universe 0-20)
# Puncak referensi: p_sr=1, p_r=3, p_s=7, p_t=12, p_st=17
serat_bahan['sangat_rendah'] = fuzz.trapmf(serat_bahan.universe, [0, 0, 1, 3])      # Rentang input efektif: 0 - 3
serat_bahan['rendah'] = fuzz.trimf(serat_bahan.universe, [1, 3, 7])                 # Rentang input efektif: 1 - 7
serat_bahan['sedang'] = fuzz.trimf(serat_bahan.universe, [3, 7, 12])                # Rentang input efektif: 3 - 12
serat_bahan['tinggi'] = fuzz.trimf(serat_bahan.universe, [7, 12, 17])               # Rentang input efektif: 7 - 17
serat_bahan['sangat_tinggi'] = fuzz.trapmf(serat_bahan.universe, [12, 17, 20, 20]) # Rentang input efektif: 12 - 20

# Output Kesehatan
kesehatan_bahan['sangat_tidak_sehat'] = fuzz.trimf(kesehatan_bahan.universe, [0, 10, 20])    # Rentang output: 0 - 20
kesehatan_bahan['tidak_sehat'] = fuzz.trimf(kesehatan_bahan.universe, [15, 30, 45])          # Rentang output: 15 - 45
kesehatan_bahan['cukup_sehat'] = fuzz.trimf(kesehatan_bahan.universe, [40, 55, 70])          # Rentang output: 40 - 70
kesehatan_bahan['sehat'] = fuzz.trimf(kesehatan_bahan.universe, [65, 80, 90])                # Rentang output: 65 - 90
kesehatan_bahan['sangat_sehat'] = fuzz.trimf(kesehatan_bahan.universe, [85, 95, 100])        # Rentang output: 85 - 100

# --- 3. PENDEFINISIAN ATURAN FUZZY (RULE BASE) ---
# (Semua 51 aturan dari rule1 hingga rule51 dengan komentar target outputnya tetap sama seperti kode lengkap sebelumnya)

# Target: Sangat Tidak Sehat - Kondisi paling buruk: kalori, lemak sangat tinggi; protein, serat sangat rendah.
rule1 = ctrl.Rule(kalori_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_tinggi'] & protein_bahan['sangat_rendah'] & serat_bahan['sangat_rendah'], kesehatan_bahan['sangat_tidak_sehat'])
# Target: Sangat Tidak Sehat - Kalori tinggi, lemak dan karbohidrat sangat tinggi.
rule2 = ctrl.Rule(kalori_bahan['tinggi'] & lemak_total_bahan['sangat_tinggi'] & karbohidrat_bahan['sangat_tinggi'], kesehatan_bahan['sangat_tidak_sehat'])
# Target: Tidak Sehat - Kalori tinggi, lemak/karbo tinggi, protein rendah.
rule3 = ctrl.Rule(kalori_bahan['tinggi'] & (lemak_total_bahan['tinggi'] | (karbohidrat_bahan['tinggi'] | karbohidrat_bahan['sangat_tinggi'])) & protein_bahan['rendah'], kesehatan_bahan['tidak_sehat'])
# Target: Tidak Sehat - Lemak sangat tinggi, serat sangat rendah, protein rendah/sangat_rendah, dan kalori tidak sangat tinggi.
rule4 = ctrl.Rule(lemak_total_bahan['sangat_tinggi'] & serat_bahan['sangat_rendah'] & (protein_bahan['sangat_rendah'] | protein_bahan['rendah']) & ~kalori_bahan['sangat_tinggi'], kesehatan_bahan['tidak_sehat'])
# Target: Tidak Sehat - Protein sangat rendah, tetapi kalori tidak sangat rendah.
rule5 = ctrl.Rule(protein_bahan['sangat_rendah'] & ~kalori_bahan['sangat_rendah'] & ~kalori_bahan['rendah'], kesehatan_bahan['tidak_sehat'])
# Target: Cukup Sehat - Profil serba sedang/cukup, serat minimal sedang atau rendah.
rule6 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['cukup'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & (serat_bahan['sedang'] | serat_bahan['rendah']), kesehatan_bahan['cukup_sehat'])
# Target: Cukup Sehat - Protein tinggi, namun lemak, kalori, serat hanya sedang.
rule7 = ctrl.Rule(protein_bahan['tinggi'] & lemak_total_bahan['sedang'] & kalori_bahan['sedang'] & serat_bahan['sedang'], kesehatan_bahan['cukup_sehat'])
# Target: Cukup Sehat - Serat sedang, kalori sedang, dan lemak tidak tinggi/sangat tinggi.
rule8 = ctrl.Rule(serat_bahan['sedang'] & kalori_bahan['sedang'] & ~(lemak_total_bahan['tinggi'] | lemak_total_bahan['sangat_tinggi']), kesehatan_bahan['cukup_sehat'])
# Target: Sehat - Protein tinggi, lemak rendah, kalori sedang/rendah, serat sedang.
rule9 = ctrl.Rule(protein_bahan['tinggi'] & (lemak_total_bahan['rendah'] | lemak_total_bahan['sangat_rendah']) & (kalori_bahan['sedang'] | kalori_bahan['rendah']) & serat_bahan['sedang'], kesehatan_bahan['sehat'])
# Target: Sehat - Profil rendah kalori, lemak, karbohidrat; dengan protein cukup dan serat tinggi.
rule10 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['cukup'] & (lemak_total_bahan['rendah'] | lemak_total_bahan['sangat_rendah']) & (karbohidrat_bahan['rendah'] | karbohidrat_bahan['sangat_rendah']) & (serat_bahan['tinggi'] | serat_bahan['sangat_tinggi']), kesehatan_bahan['sehat'])
# Target: Sangat Sehat - Protein tinggi/sangat tinggi, lemak sangat rendah, karbohidrat dan kalori rendah.
rule11 = ctrl.Rule((protein_bahan['tinggi'] | protein_bahan['sangat_tinggi']) & lemak_total_bahan['sangat_rendah'] & (karbohidrat_bahan['rendah'] | karbohidrat_bahan['sangat_rendah']) & (kalori_bahan['rendah'] | kalori_bahan['sangat_rendah']), kesehatan_bahan['sangat_sehat'])
# Target: Sangat Sehat - Profil ideal rendah kalori, lemak, karbohidrat; dengan protein dan serat sangat tinggi.
rule12 = ctrl.Rule(protein_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_rendah'] & (kalori_bahan['rendah'] | kalori_bahan['sangat_rendah']) & karbohidrat_bahan['sangat_rendah'] & (serat_bahan['tinggi'] | serat_bahan['sangat_tinggi']), kesehatan_bahan['sangat_sehat'])
# Target: Sangat Sehat - Kalori sangat rendah, protein tinggi, lemak sangat rendah, serat dan karbohidrat baik.
rule13 = ctrl.Rule(kalori_bahan['sangat_rendah'] & (protein_bahan['tinggi'] | protein_bahan['sangat_tinggi']) & lemak_total_bahan['sangat_rendah'] & (serat_bahan['sedang'] | serat_bahan['tinggi'] | serat_bahan['sangat_tinggi']) & (karbohidrat_bahan['sangat_rendah'] | karbohidrat_bahan['rendah']), kesehatan_bahan['sangat_sehat'])
# Target: Sehat - Kalori rendah, protein cukup/tinggi, lemak sedang, karbohidrat rendah, serat tinggi.
rule14 = ctrl.Rule(kalori_bahan['rendah'] & (protein_bahan['cukup'] | protein_bahan['tinggi']) & lemak_total_bahan['sedang'] & karbohidrat_bahan['rendah'] & (serat_bahan['tinggi'] | serat_bahan['sangat_tinggi']), kesehatan_bahan['sehat'])
# Target: Sehat - Kalori, lemak, karbo sedang; namun protein dan serat sangat tinggi.
rule15 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['sangat_tinggi'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & serat_bahan['sangat_tinggi'], kesehatan_bahan['sehat'])
# Target: Cukup Sehat - Kalori sedang, protein & serat tinggi, karbo rendah, TAPI lemak tinggi.
rule16 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['tinggi'] & lemak_total_bahan['tinggi'] & karbohidrat_bahan['rendah'] & serat_bahan['tinggi'], kesehatan_bahan['cukup_sehat'])
# Target: Tidak Sehat - Serba sedang, tapi protein dan serat rendah.
rule17 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['rendah'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & serat_bahan['rendah'], kesehatan_bahan['tidak_sehat'])
# Target: Tidak Sehat - Semua nutrisi sangat rendah (kosong secara nutrisi).
rule18 = ctrl.Rule(kalori_bahan['sangat_rendah'] & protein_bahan['sangat_rendah'] & lemak_total_bahan['sangat_rendah'] & karbohidrat_bahan['sangat_rendah'] & serat_bahan['sangat_rendah'], kesehatan_bahan['tidak_sehat'])
# Target: Tidak Sehat - Kalori & karbohidrat tinggi, meskipun protein, lemak, serat sedang/cukup.
rule19 = ctrl.Rule(kalori_bahan['tinggi'] & protein_bahan['cukup'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['tinggi'] & serat_bahan['sedang'], kesehatan_bahan['tidak_sehat'])
# Target: Sangat Sehat - Profil sangat baik: kalori sedang, protein & serat sangat tinggi, lemak rendah, karbo sedang.
rule20 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['sangat_tinggi'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['sedang'] & serat_bahan['sangat_tinggi'], kesehatan_bahan['sangat_sehat'])
# Target: Cukup Sehat - Nutrisi lain sempurna, tapi kalori sangat tinggi.
rule21 = ctrl.Rule(kalori_bahan['sangat_tinggi'] & protein_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_rendah'] & karbohidrat_bahan['sangat_rendah'] & serat_bahan['sangat_tinggi'], kesehatan_bahan['cukup_sehat'])
# Target: Cukup Sehat - Kalori rendah, protein cukup, lemak sedang, karbohidrat rendah, serat sedang.
rule22 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['cukup'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['rendah'] & serat_bahan['sedang'], kesehatan_bahan['cukup_sehat'])
# Target: Sehat - Kalori rendah, protein tinggi, lemak sedang, karbohidrat rendah, serat tinggi.
rule23 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['tinggi'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['rendah'] & serat_bahan['tinggi'], kesehatan_bahan['sehat'])
# Target: Tidak Sehat - Lemak sangat tinggi, meskipun protein dan serat cukup/baik.
rule24 = ctrl.Rule(lemak_total_bahan['sangat_tinggi'] & (protein_bahan['cukup'] | protein_bahan['tinggi'] | protein_bahan['sangat_tinggi']) & (serat_bahan['sedang'] | serat_bahan['tinggi'] | serat_bahan['sangat_tinggi']), kesehatan_bahan['tidak_sehat'])
# Target: Sehat - Kalori sedang, Protein tinggi, Lemak sedang, Karbohidrat rendah, Serat tinggi.
rule25 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['tinggi'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['rendah'] & serat_bahan['tinggi'], kesehatan_bahan['sehat'])
# Target: Sehat - Kalori rendah, Protein cukup, Lemak rendah, Karbohidrat sedang, Serat sedang.
rule26 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['cukup'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['sedang'] & serat_bahan['sedang'], kesehatan_bahan['sehat'])
# Target: Tidak Sehat - Kalori tinggi, Protein tinggi, Lemak sedang, Karbohidrat tinggi, Serat sedang.
rule27 = ctrl.Rule(kalori_bahan['tinggi'] & protein_bahan['tinggi'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['tinggi'] & serat_bahan['sedang'], kesehatan_bahan['tidak_sehat'])
# Target: Cukup Sehat - Semua sedang kecuali Lemak tinggi.
rule28 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['cukup'] & lemak_total_bahan['tinggi'] & karbohidrat_bahan['sedang'] & serat_bahan['sedang'], kesehatan_bahan['cukup_sehat'])
# Target: Sangat Tidak Sehat - Kalori sangat tinggi, Lemak sangat tinggi, lainnya sedang/baik.
rule29 = ctrl.Rule(kalori_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_tinggi'] & (protein_bahan['cukup'] | protein_bahan['tinggi']) & karbohidrat_bahan['sedang'] & (serat_bahan['sedang'] | serat_bahan['tinggi']), kesehatan_bahan['sangat_tidak_sehat'])
# Target: Sangat Sehat - Lemak & Karbo sangat rendah, Serat sangat tinggi, Protein tinggi, Kalori sedang.
rule30 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['tinggi'] & lemak_total_bahan['sangat_rendah'] & karbohidrat_bahan['sangat_rendah'] & serat_bahan['sangat_tinggi'], kesehatan_bahan['sangat_sehat'])
# Target: Sangat Tidak Sehat - Kalori tinggi, Protein sangat rendah, Lemak tinggi, Karbohidrat tinggi, Serat sangat rendah.
rule31 = ctrl.Rule(kalori_bahan['tinggi'] & protein_bahan['sangat_rendah'] & lemak_total_bahan['tinggi'] & karbohidrat_bahan['tinggi'] & serat_bahan['sangat_rendah'], kesehatan_bahan['sangat_tidak_sehat'])
# Target: Cukup Sehat - Kalori rendah, Protein tinggi, Lemak rendah, TAPI Karbohidrat tinggi, Serat sedang.
rule32 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['tinggi'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['tinggi'] & serat_bahan['sedang'], kesehatan_bahan['cukup_sehat'])
# Target: Sehat - Kalori sedang, Protein cukup, Lemak sedang, Karbohidrat sangat rendah, Serat sangat tinggi.
rule33 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['cukup'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sangat_rendah'] & serat_bahan['sangat_tinggi'], kesehatan_bahan['sehat'])
# Target: Cukup Sehat - Kalori sedang, Protein rendah, Lemak rendah, Karbohidrat rendah, Serat rendah.
rule34 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['rendah'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['rendah'] & serat_bahan['rendah'], kesehatan_bahan['cukup_sehat'])
# Target: Tidak Sehat - Kalori tinggi, Protein, Lemak, Karbo, Serat SANGAT TINGGI SEMUA.
rule35 = ctrl.Rule(kalori_bahan['tinggi'] & protein_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_tinggi'] & karbohidrat_bahan['sangat_tinggi'] & serat_bahan['sangat_tinggi'], kesehatan_bahan['tidak_sehat'])
# Target: Sehat - Kalori rendah, Protein sangat tinggi, Lemak sedang, Karbohidrat sedang, Serat tinggi.
rule36 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['sangat_tinggi'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & serat_bahan['tinggi'], kesehatan_bahan['sehat'])
# Target: Cukup Sehat - Kalori rendah, Protein rendah, Lemak rendah, Karbohidrat rendah, Serat tinggi.
rule37 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['rendah'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['rendah'] & serat_bahan['tinggi'], kesehatan_bahan['cukup_sehat'])
# Target: Cukup Sehat - Kalori rendah, Protein cukup, Lemak tinggi, Karbohidrat sedang, Serat sedang.
rule38 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['cukup'] & lemak_total_bahan['tinggi'] & karbohidrat_bahan['sedang'] & serat_bahan['sedang'], kesehatan_bahan['cukup_sehat'])
# Target: Tidak Sehat - Kalori sedang, Protein tinggi, Lemak tinggi, Karbohidrat tinggi, Serat rendah.
rule39 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['tinggi'] & lemak_total_bahan['tinggi'] & karbohidrat_bahan['tinggi'] & serat_bahan['rendah'], kesehatan_bahan['tidak_sehat'])
# Target: Tidak Sehat - Kalori sedang, Protein sangat rendah, Lemak sedang, Karbohidrat sedang, Serat sedang.
rule40 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['sangat_rendah'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & serat_bahan['sedang'], kesehatan_bahan['tidak_sehat'])
# Target: Cukup Sehat - Kalori tinggi, TAPI Protein tinggi, Lemak rendah, Karbohidrat rendah, Serat sangat tinggi.
rule41 = ctrl.Rule(kalori_bahan['tinggi'] & protein_bahan['tinggi'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['rendah'] & serat_bahan['sangat_tinggi'], kesehatan_bahan['cukup_sehat'])
# Target: Tidak Sehat - Kalori tinggi, Protein cukup, Lemak sedang, Karbohidrat sedang, Serat rendah.
rule42 = ctrl.Rule(kalori_bahan['tinggi'] & protein_bahan['cukup'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & serat_bahan['rendah'], kesehatan_bahan['tidak_sehat'])
# Target: Cukup Sehat - Lemak tinggi, TAPI Kalori rendah, Protein tinggi, Karbohidrat sangat rendah, Serat sangat tinggi.
rule43 = ctrl.Rule(lemak_total_bahan['tinggi'] & kalori_bahan['rendah'] & protein_bahan['tinggi'] & karbohidrat_bahan['sangat_rendah'] & serat_bahan['sangat_tinggi'], kesehatan_bahan['cukup_sehat'])
# Target: Sangat Tidak Sehat - Lemak sangat tinggi, Kalori sedang, Protein rendah, Karbohidrat sedang, Serat rendah.
rule44 = ctrl.Rule(lemak_total_bahan['sangat_tinggi'] & kalori_bahan['sedang'] & protein_bahan['rendah'] & karbohidrat_bahan['sedang'] & serat_bahan['rendah'], kesehatan_bahan['sangat_tidak_sehat'])
# Target: Cukup Sehat - Karbohidrat tinggi, TAPI Kalori rendah, Protein tinggi, Lemak rendah, Serat tinggi.
rule45 = ctrl.Rule(karbohidrat_bahan['tinggi'] & kalori_bahan['rendah'] & protein_bahan['tinggi'] & lemak_total_bahan['rendah'] & serat_bahan['tinggi'], kesehatan_bahan['cukup_sehat'])
# Target: Sangat Tidak Sehat - Karbohidrat sangat tinggi, Kalori sedang, Protein rendah, Lemak sedang, Serat rendah.
rule46 = ctrl.Rule(karbohidrat_bahan['sangat_tinggi'] & kalori_bahan['sedang'] & protein_bahan['rendah'] & lemak_total_bahan['sedang'] & serat_bahan['rendah'], kesehatan_bahan['sangat_tidak_sehat'])
# Target: Sangat Sehat - Hampir sempurna, tapi serat hanya sedang.
rule47 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_rendah'] & karbohidrat_bahan['sangat_rendah'] & serat_bahan['sedang'], kesehatan_bahan['sangat_sehat'])
# Target: Cukup Sehat - Kalori sedang, Protein cukup, Lemak rendah, Karbohidrat sedang, TAPI Serat rendah.
rule48 = ctrl.Rule(kalori_bahan['sedang'] & protein_bahan['cukup'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['sedang'] & serat_bahan['rendah'], kesehatan_bahan['cukup_sehat'])
# Target: Cukup Sehat - Kalori rendah, Protein rendah, Lemak sedang, Karbohidrat sedang, Serat sedang.
rule49 = ctrl.Rule(kalori_bahan['rendah'] & protein_bahan['rendah'] & lemak_total_bahan['sedang'] & karbohidrat_bahan['sedang'] & serat_bahan['sedang'], kesehatan_bahan['cukup_sehat'])
# Target: Sehat - Kalori sangat rendah, Protein cukup, Lemak rendah, Karbohidrat rendah, Serat sedang.
rule50 = ctrl.Rule(kalori_bahan['sangat_rendah'] & protein_bahan['cukup'] & lemak_total_bahan['rendah'] & karbohidrat_bahan['rendah'] & serat_bahan['sedang'], kesehatan_bahan['sehat'])
# Target: Sangat Tidak Sehat - Variasi dari rule2 untuk Kalori Sangat Tinggi.
rule51 = ctrl.Rule(kalori_bahan['sangat_tinggi'] & lemak_total_bahan['sangat_tinggi'] & karbohidrat_bahan['sangat_tinggi'], kesehatan_bahan['sangat_tidak_sehat'])

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

# --- 5. FUNGSI UTAMA UNTUK MENGHITUNG (dengan Logika Fallback dan Debugging Aturan yang Disempurnakan) ---
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

        print("\n--- LOGIC.PY: DEBUGGING DETAIL AKTIVASI ATURAN ---")
        if hasattr(penilaian_simulasi, 'rule_activation'):
            rule_name_map = {id(rule_obj): name for name, rule_obj in globals().items() if isinstance(rule_obj, ctrl.Rule)}
            print("  Raw rule_activation dictionary (key: rule_object_id, value: activation):")
            readable_activations = {}
            for rule_obj_key, act_val in penilaian_simulasi.rule_activation.items():
                found_name = "UnknownRuleObject"
                for name, global_rule_obj in rule_name_map.items():
                    if global_rule_obj is rule_obj_key:
                        found_name = name
                        break
                if found_name == "UnknownRuleObject":
                     try:
                        idx = -1 # Inisialisasi idx
                        for i_list, r_in_list in enumerate(all_rules): # Pastikan all_rules terdefinisi di scope ini atau global
                            if r_in_list is rule_obj_key:
                                idx = i_list
                                break
                        if idx != -1:
                            temp_name = [var_name for var_name, var_obj in globals().items() if var_obj is all_rules[idx]]
                            if temp_name: found_name = temp_name[0]
                            else: found_name = f"all_rules[{idx}]"
                        else: found_name = f"RuleObject_{id(rule_obj_key)}"
                     except NameError: # Jika all_rules tidak terdefinisi di scope ini (seharusnya tidak terjadi jika global)
                         found_name = f"RuleObject_{id(rule_obj_key)} (all_rules not found)"
                     except ValueError: 
                         found_name = f"RuleObject_{id(rule_obj_key)} (not in all_rules)"
                readable_activations[found_name] = f"{act_val:.6f}"
            print(f"  {readable_activations}")
        else:
            print("  Objek penilaian_simulasi tidak memiliki atribut 'rule_activation'.")

        print("\n  Aktivasi per Aturan (untuk semua aturan dalam sistem kontrol):")
        any_rule_fired_significantly = False
        if penilaian_ctrl_system is not None and hasattr(penilaian_simulasi, 'rule_activation'):
            rule_name_map_iter = {id(rule_obj): name for name, rule_obj in globals().items() if isinstance(rule_obj, ctrl.Rule)} # Definisikan di sini juga
            for i, rule_obj_iter in enumerate(penilaian_ctrl_system.rules):
                activation = penilaian_simulasi.rule_activation.get(rule_obj_iter, 0.0)
                rule_readable_name_iter = "UnknownRule"
                for rule_id_map, name_map_val in rule_name_map_iter.items(): # Gunakan map yang baru dibuat
                    if rule_id_map == id(rule_obj_iter):
                        rule_readable_name_iter = name_map_val
                        break
                if rule_readable_name_iter == "UnknownRule":
                     rule_readable_name_iter = f"Aturan_Index-{i}"

                consequent_label = "UnknownConsequent"
                if rule_obj_iter.consequent and rule_obj_iter.consequent[0].label:
                    consequent_label = rule_obj_iter.consequent[0].label
                
                is_problem_input_sk1 = (val_kalori == 750 and val_protein == 3 and val_lemak == 45 and val_karbo == 90 and val_serat == 1)
                is_problem_input_sk3 = (val_kalori == 400 and val_protein == 15 and val_lemak == 20 and val_karbo == 50 and val_serat == 5)

                if is_problem_input_sk1 or is_problem_input_sk3 or activation > 1e-9:
                    print(f"    -> [{rule_readable_name_iter}] (Target: {consequent_label}), Aktivasi: {activation:.6f}")
                    if activation > 1e-9:
                        any_rule_fired_significantly = True
        
        if not any_rule_fired_significantly:
            print("  Tidak ada aturan yang terpicu dengan aktivasi signifikan (> 1e-9).")
        print("--- LOGIC.PY: AKHIR DEBUGGING DETAIL AKTIVASI ATURAN ---\n")
        
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
            print(f"LOGIC.PY: Output standar tidak ditemukan/NaN. Mencoba pendekatan aturan terdekat...")
            max_activation = 0.0
            best_kategori_label_from_fallback = None
            category_to_score_map = {
                "sangat_tidak_sehat": 10, "tidak_sehat": 30, "cukup_sehat": 55,
                "sehat": 80, "sangat_sehat": 95 
            }
            rule_fired_in_fallback = False
            if hasattr(penilaian_simulasi, 'rule_activation') and penilaian_ctrl_system is not None:
                for rule_obj in penilaian_ctrl_system.rules:
                    activation = penilaian_simulasi.rule_activation.get(rule_obj, 0.0)
                    if activation > max_activation:
                        max_activation = activation
                        if rule_obj.consequent and rule_obj.consequent[0].label:
                            best_kategori_label_from_fallback = rule_obj.consequent[0].label
                            rule_fired_in_fallback = True
            
            if rule_fired_in_fallback and best_kategori_label_from_fallback is not None and max_activation > 0.001: 
                print(f"LOGIC.PY: Pendekatan: Aturan terdekat teraktivasi {max_activation:.4f}, kategori tentative: {best_kategori_label_from_fallback}")
                kategori_display = best_kategori_label_from_fallback.replace("_", " ").title()
                kategori_label_final = f"{kategori_display} (Pendekatan)"
                skor_hasil_final = category_to_score_map.get(best_kategori_label_from_fallback, skor_hasil_default)
                simulasi_untuk_plot = penilaian_simulasi 
            else:
                if output_kesehatan is not None and np.isnan(output_kesehatan) :
                     kategori_label_final = "Tidak Terdefinisi (Aktivasi Sangat Rendah)"
                else: 
                     kategori_label_final = kategori_label_default 
                skor_hasil_final = skor_hasil_default
                print(f"LOGIC.PY: Pendekatan gagal: Aktivasi maksimal ({max_activation:.4f}) terlalu rendah atau tidak ada aturan terpicu. Kategori: {kategori_label_final}")

        if show_plot and simulasi_untuk_plot is not None:
            print("LOGIC.PY: Menyiapkan plot...")
            try:
                plt.figure() 
                kesehatan_bahan.view(sim=simulasi_untuk_plot)
                plt.title(f"Plot Fuzzy: K{val_kalori},P{val_protein},L{val_lemak},Kr{val_karbo},S{val_serat}")
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