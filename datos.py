class ADN:
    def __init__(self):
        self.adn_list = []
        self.filas = ["la primera", "la segunda", "la tercera", "la cuarta", "la quinta", "la sexta"]

    def ingresar_adn(self):
        for i in range(6):
            value = input(f"Ingresa {self.filas[i]} de tu ADN: ")
            self.adn_list.append(value)
    adn = []
    adn.ingresar_adn()
    print("ADN ingresado:", adn.adn_list) 



