fjson = "6_taller/data.json"
fcsv = "4_taller/users.csv"
import json
import csv

def convert():
    with open(fcsv, "r") as file:
        reader = csv.DictReader(file)
        try:    
            with open(fjson, "w") as json_file:
                json.dump(list(reader), json_file, indent=2)
                print("CSV to JSON conversion completed successfully.")
                input("continue...")
        except Exception as e:
            print(f"Error converting CSV to JSON: {e}")
        
while True:
    print("1. Convert JSON to CSV")
    op = int(input("Choose an option: "))
    if op == 1:
        convert()
    elif op == 2:
        break
    else:
        print("Invalid option")
