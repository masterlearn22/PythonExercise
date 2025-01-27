    
    
def txt():
     file_path ="files/infoFiles.txt"
     
     with open (file_path, mode="r") as f:
         for line in f:
             print(line, end="")
             
txt()

def json():    
    import json
    file_path ="files/informasi.json"

    with open (file_path, 'r') as file:
        data = json.load(file)
        print(json.dumps(data, indent=4))
        
def csv():
    import csv
    
    file_path ="files/informasi.csv"
    
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            
csv()


    