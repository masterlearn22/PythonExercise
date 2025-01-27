import datetime
import time
import pygame
import threading

def advance_alarm(*arg):
     
    def set_alarm(alarm_time,**kwarg):
        print(f"Alarm diatur untuk {alarm_time}")
        sound_file = "mini_project/xtali.mp3"
        
        def play_alarm():
            pygame.mixer.init()  # inisialisasi mixer
            pygame.mixer.music.load(sound_file)  # load file musik
            pygame.mixer.music.play(loops=-1)  # mainkan musik, dengan loop -1 untuk mainkan musik secara terus menerus
            
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time, end="\r")
            
            if current_time == alarm_time:
                print("\nWake Up! It's time to wake up!")
                # Memulai pemutaran alarm dalam thread terpisah
                alarm_thread = threading.Thread(target=play_alarm)  # membuat thread
                alarm_thread.start()
                # Thread utama: Menjalankan penghitungan waktu (menghitung detik yang telah berlalu sejak alarm dimulai).
                # Thread baru (alarm_thread): Memainkan musik alarm secara terus-menerus sampai pengguna menekan tombol "Enter" untuk menghentikannya.

                start_time = datetime.datetime.now()  # Catat waktu mulai
                elapsed_time = 0  # Inisialisasi penghitung waktu
                
                waktu_berhenti = start_time + datetime.timedelta(seconds=10)
                sisa_waktu = (waktu_berhenti - start_time).total_seconds()
                print (f"Alarm berhenti dalam {sisa_waktu:.2f} detik")# Waktu berhenti alarm (10 detik)
                
                while True:
                    elapsed_time = (datetime.datetime.now() - start_time).total_seconds() 
                    print(f"Alarm berbunyi selama {elapsed_time:.2f} detik", end="\r")
                    
                    # Cek jika pengguna menekan enter untuk berhenti alarm atau waktu berhenti sudah tercapai
                    if datetime.datetime.now() >= waktu_berhenti:
                        pygame.mixer.music.stop()
                        pygame.mixer.quit()
                        break

                    time.sleep(0.1)  # Menunggu sebentar untuk menghindari penggunaan CPU berlebihan

                break
            time.sleep(1)
    set_alarm(alarm_time) 
    
def simple_alarm(*arg):
    import datetime
    import time
    import pygame

     
    def set_alarm(alarm_time):
        print(f"Alarm diatur untuk {alarm_time}")
        sound_file = "mini_project/xtali.mp3"

        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time, end="\r")
            if current_time == alarm_time:
                print("\nWake Up! It's time to wake up!")
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play(loops=-1)
                input("Tekan Enter untuk menghentikan alarm...")
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                break
            time.sleep(1)
    set_alarm(alarm_time)


if __name__ == "__main__":
    # Menambahkan 10 detik ke waktu saat ini
    alarm_time = datetime.datetime.now() + datetime.timedelta(seconds=2)
    print(alarm_time)
    alarm_time = alarm_time.strftime("%H:%M:%S")  # Format waktu menjadi string HH:MM:SS
    pilih =1
    if pilih == 1:
        print("Alarm 1")
        advance_alarm(alarm_time,)
    elif pilih == 2:
        simple_alarm(alarm_time)
        