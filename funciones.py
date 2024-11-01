from ejecutable import MenuPrincipal
class Guia:
    def __init__(self):
        print("""
-La secuencia del ADN se ingresa de izquierda a derecha.
-El ADN elegido se ingresa por filas (con un maximo de 6 bases nitrogenadas).
  A G A T C A - Fila 1
  G A T T C A - Fila 2
  C A A C A T - Fila 3
  G A G C T A - Fila 4
  A T T G C G - Fila 5
  C T G T T C - Fila 6

Si desea volver presione 1, si desea salir del programa pulse 0:
            """)
        choice = int(input())
        match choice:
            case 0:
                print("Gracias por utilizar nuestro programa, Hasta Luego!.")
                pass
            case 1:
                print("Volviendo al menu princial.")
                MenuPrincipal()
            case other:
                print("Elige una opcion en pantalla.")
                Guia()