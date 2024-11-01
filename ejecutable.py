from funciones import *
from datos import *
class MenuPrincipal:
    def __init__(self):
        print("""
      1) Guía
      2) Ingresar ADN
      3) Detector
      4) Mutador
      5) Radiación
      6) Virus
      7) Sanador
      0) Salir del programa
      """)
    choice = int(input())
    match choice:
        case 1:
            Guia()
        case 2:
            ADN()
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 0:
            print("Saliendo del programa...")
        case other:
            print("Opción no válida, elige una opcion en pantalla:")
            MenuPrincipal()
if __name__ == "__main__":
    print("Bienvenido, para utilizar el programa ingrese de manera numérica la tarea a realizar:")
    MenuPrincipal()
