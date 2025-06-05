fichero = "2_taller/diario.txt"
import os

date = "Fecha: 2025-06-02"
busy = False

def leerDiario():
    with open(fichero, mode="r") as file:
        diario = file.readlines()
    for i in diario:
        print(f"{i}")
    return diario

def escribirDiario(msg):
    with open(fichero, mode="a") as file:
        file.writelines(f"\n{msg}")

with open(fichero, "a") as filee:
    filee.writelines(f"\n{date}")

menu = """
𝑸𝒖𝒆𝒓𝒊𝒅𝒐  𝑫 𝒊𝒂𝒓𝒊𝒐
(Dario personal, NO abrir)

1. Leer diario.
2. Escribir nueva linea.
3. Cerrar diario.

"""

while True:
    print(menu)
    op = int(input("Ingresar opcion: "))
    if op == 1:
        leerDiario()
        input("Continuar...")
        continue
    elif op == 2:
        inp = input("Ingresar nota: ")
        escribirDiario(inp)
    elif op == 3:
        break
    else:
        print("[X] Opcion no valida.")