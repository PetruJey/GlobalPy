class ADN:
    #Se solicita cada una de las filas del ADN al usuario y se guarda cada fila como un String.
    #En caso de ya existir un ADN guardado, el programa
    adn_list = []
    filas = ("la primera", "la segunda", "la tercera", "la cuarta", "la quinta", "la sexta")
    def __init__(self):
        self.adn_list = []
        self.filas = ()
    if adn_list == []:
        for i in range(0, 6):
            value = input(f"Ingresa {filas[i]} fila de tu ADN: ")
            adn_list.append(value)
    else:
        print("Ya existe un ADN Guardado:")
    print(f"ADN: "+adn_list)