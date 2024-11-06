from funciones import *
adn_list = []
while True:
    print("""
    **Menú principal**
        1) Guía
        2) Ingresar ADN
        3) Detector
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
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Elija una opción en pantalla.")