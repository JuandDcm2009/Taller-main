fichero = "1_taller/notas.txt"

def cartelera():
    print(" 𝗖𝗮𝗿𝘁𝗲𝗹𝗲𝗿𝗮 \n")
    try:
        with open(fichero, mode="r") as file:
                cartelera = file.readlines()

        for i in cartelera:
                print(i)
    except FileNotFoundError:
        print("[X] Oh No! no puede ser, como puede ser posbile ):... al parecer no se encuentran las peliculas.. deben estar rayados los Cd`s")


menu = """

 █▀▀ █ █▄░█ █▀▀
 █▄▄ █ █░▀█ ██▄

Biembenido al cine!

    1. Mostrar cartelera.
    2. Salir.

"""


while True:
    print(menu)

    opcion = int(input("Ingresar una Opcion: "))
    if opcion == 1:
        print("\n")
        cartelera()
        input("Continuar..")
        continue
    elif opcion == 2:
        break
    else:
        print("[X] Opcion no valida.") 