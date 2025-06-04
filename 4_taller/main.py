import csv
fichero = "4_taller/users.csv"
data = [
    {
        "id": 1,
        "name": "Juan",
        "city": "Bogota"
    },
    {
        "id": 2,
        "name": "Sofia",
        "city": "bucaramanga"
    },
    {
        "id": 3,
        "name": "Pedro",
        "city": "medellin"
    }
]

campos = ["id", "name", "city"]
 

def changeCity(inp):
    for i in range(len(data)):
        if inp == data[i]["id"]: 
            try: 
                with open(fichero, "w", newline="") as file:
                    text = input("Input the city: ")
                    try:
                        data[inp - 1]["city"] = text
                        datosAc = csv.DictWriter(file, fieldnames=campos)
                        datosAc.writeheader()
                        datosAc.writerows(data)
                        print("Saved")
                    except FileNotFoundError: 
                        print("Error, file not found")
            except FileNotFoundError:
                print("Error, file not found.")

def printList():
    try:
        with open(fichero, "r") as file:
            print(file.read())
        changeCity(int(input("Input the user id: ")))
    except FileNotFoundError:
                print("Error, file not found.")

menu = """
Citys
1. Change city.
2. Exit.
"""

while True:

    print(menu)
    op = int(input("Input option: "))
    if op == 1:
        printList()
    if op == 2:
        break
    else:
        pass