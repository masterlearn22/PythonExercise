import threading 
import time


def learn_python():
    time.sleep(10)
    print("Learning Python...")
    
    
def pull_up():
    set= 0
    while set < 5:
        time.sleep(3)
        set += 1
        print(f"Pulling up set {set}...")
        
def run(set):
    i=0
    while i < set:
        time.sleep(4)
        i += 1
        print(f"Running set {i}...")


actv1 = threading.Thread(target=learn_python)
actv1.start()
actv2 = threading.Thread(target=pull_up)
actv2.start()
actv3 = threading.Thread(target=run,args=(5,))
actv3.start()

actv1.join()
actv2.join()
actv3.join()
print("Semua Aktivitas Selesai")

