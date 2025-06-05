datos = []
name = input("Ingrese el nombre de la persona: ")
age = int(input("Ingrese la edad de la persona: "))

datos.append({"name": name, "age": age})

print(f"Nombre: {datos[0]["name"]} - Edad: {datos[0]["age"]}")