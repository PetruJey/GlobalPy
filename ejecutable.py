from clases import *
from funciones import *
adn_list = []
while True: #Lista de opciones a elegir
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
        guia() #Muestra una guia de como se deberia ingresar el adn
    elif choice == "2":
        ingresar_adn(adn_list) #Llama a la funcion para ingresar una lista de adn
    elif choice == "3":
        deteccion = Detector(adn_list) #Llama a la clase Detector y pasa una lista de and
    elif choice == "4":
        mutar = Mutador(adn_list)  #Llama a la clase Mutador
        seleccion = mutar.Saludo()  #Recibe el resultado de Mutador y dependiendo de este pasa lo siguiente
        if seleccion == 1:
            radiar = Radiacion(adn_list) #Llama a la clase Radiacion y le pasa una lista de adn
        elif seleccion == 2:
            virus = Virus(adn_list) #Llama a la clase Virus y le pasa una lsita de adn
        elif seleccion == 0:
            continue  #Sigue con el bucle
    elif choice == "5":
        sanador = Sanador(adn_list) #Llama a la clase Sanador y le pasa una lista de adn
        adn_list = sanador.analizar_mutaciones() #Recibe el resultado de la clase
    elif choice == "0":
        print("Saliendo del programa...") #Termina la ejecucion del programa
        break
    else:
        print("Elija una opción en pantalla.") #En caso de error