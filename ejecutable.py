from clases import *
from funciones import *
adn_list = []
while True:
    print("""
    **Menú principal**
        1) Guía
        2) Ingresar ADN
        3) Detector de Mutaciones
        4) Mutador
        5) Sanador
        0) Salir del programa
        """)
    choice = str(input())
    if choice == "1":
        guia()
    elif choice == "2":
        ingresar_adn(adn_list)
    elif choice == "3":
        deteccion = Detector(adn_list)
    elif choice == "4":
        mutar = Mutador(adn_list)  # Pasar la lista al constructor
        seleccion = mutar.Saludo()  # Capturar la selección del usuario
        if seleccion == 1:
            radiar = Radiacion(adn_list)
        elif seleccion == 2:
            virus = Virus(adn_list)
        elif seleccion == 0:
            continue  # Volver al menú principal
    elif choice == "5":
        sanador = Sanador(adn_list)
        adn_list = sanador.analizar_mutaciones()
    elif choice == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Elija una opción en pantalla.")