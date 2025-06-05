import json
fetch = "5_taller/productos.json"
almacen = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 1000
    },
    {
        "id": 2,
        "name": "Monitor",
        "price": 400
    },
    {
        "id": 3,
        "name": "Mouse",
        "price": 25
    }

]



def saveProducts():
    with open(fetch, "w") as file:
        json.dump(almacen, file, indent=2)

def addProduct():
    with open(fetch, "r") as file:
        products = json.load(file)
        print(products)

    for i in range(len(products)):
        id = int(input("Input pruduct ID: "))
        name = str(input("Input product name: "))
        price = float(input("Input product price: "))

        if products[i]["id"] == id:
            print("Product ID already exists.")
            input("Continue...")
            break
        elif products[i]["id"] != id:
            try:
                almacen.append({"id": id,"name": name, "price": price})
                saveProducts()
                print("Product added successfully.")
                print(f"ID: {id}\nName: {name}\nPrice: {price}")
                input("Continue...")
                break
            except json.JSONDecodeError:
                print("Error saving product. Please try again.")
                input("Continue...")
                break

def seeProducts():
    with open(fetch, "r") as file:
        products = json.load(file)
        for product in products:
            print(f"ID: {product['id']} - Name: {product['name']} - Price: {product['price']}")
    input("Continue...")

def removeProduct():
    with open(fetch, "r") as file:
        products = json.load(file)
    id = int(input("Input product ID to remove: "))
    for i in range(len(almacen)):
        if almacen[i]["id"] == id:
            del almacen[i]
            saveProducts()
            print("Product removed successfully.")
            saveProducts()
            input("Continue...")
            break
        else:
            print("Priduct ID not found.")
            input("Continue...")
            break

saveProducts()
menu = """"
Products

1. Add product.
2. see products.
3. Remove product.
4. Exit.
"""

while True:
    print(menu)
    op = int(input("Input option: "))
    if op == 1:
        addProduct()
    elif op == 2:
        seeProducts()
    elif op == 3:
        removeProduct()
    elif op == 4:
        break
    else:
        print("Invalid option.")
