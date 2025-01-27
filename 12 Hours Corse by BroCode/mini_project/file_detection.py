import os

def detect_files():
    
    print("Current working directory:", os.getcwd())

    file_path_relatif = "mini_project/test.txt"
    file_path_absolut = "D:/Personal/Belajar Ngoding/Python/mini_project/diceS_roller.py"
    random_file = "mini_project"

    if os.path.exists(file_path_relatif):
        print(f"File {file_path_relatif} relatif DITEMUKAN")
    else:
        print(f"File RELATIF TIDAK DITEMUKAN ")
        
    if os.path.exists(file_path_absolut):
        print(f"File {file_path_absolut} absolut DITEMUKAN")
    else:
        print(f"File ABSOLUT TIDAK DITEMUKAN ")
        
    if os.path.isfile(random_file):
        print(f"{random_file} adalah sebuah File")
    elif os.path.isdir(random_file):
        print(f"{random_file} adalah sebuah Folder")
        
detect_files()
