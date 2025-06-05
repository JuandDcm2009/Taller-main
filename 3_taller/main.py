fetch = "3_taller/datos.json"
import json
lista = [
    {
        "id": 1,
        "name": "Juan",
        "City": "Bogota"
    },
        {
        "id": 1,
        "name": "Sofia",
        "City": "Bogota"
    },
        {
        "id": 1,
        "name": "Alberto",
        "City": "Bucaramanga"
    },
        {
        "id": 1,
        "name": "Rodolfo",
        "City": "Cali"
    },
        {
        "id": 1,
        "name": "Maria",
        "City": "Bogota"
    },
        {
        "id": 1,
        "name": "Paola",
        "City": "Medellin"
    },
]

def saveData():
    with open(fetch, "w") as file:
        json.dump(lista, file, indent=2)
saveData()

def bogota():
    bogota_list = []
    for i in lista:
        if i["City"] == "Bogota":
            bogota_list.append(i)
    return bogota_list

print(f"Lista de personas de Bogota:  ")
for i in bogota():
    print(f"{i['name']} vive en {i['City']}")
