import random
class Detector: # Clase encargada de detectar mutaciones
class Detector: # Clase encargada de detectar mutaciones
    SaludarD= "Bienvenido al Detector de Mutaciones"
    def __init__(self, adn_list):
        try:
            self.adn_list = adn_list
            self.mutacion = False
            self.mutacion_horizontal = 0
            self.mutacion_vertical = 0
            self.mutacion_diagonal = 0
            print("Analizando ADN...")
            self.analizar_mutaciones()  # Llama a los métodos del análisis
            self.analizar_mutaciones()  # Llama a los métodos del análisis
            self.resumen()
        except IndexError:
            print("Primero debe ingresar el ADN")

    def detectar_mutantes_horizontal(self):
        for i in range(len(self.adn_list)):
            cadena = self.adn_list[i]
            for j in range(len(cadena) - 3):  # Verificar 4 caracteres antes del final
            for j in range(len(cadena) - 3):  # Verificar 4 caracteres antes del final
                if cadena[j] == cadena[j+1] == cadena[j+2] == cadena[j+3]:
                    self.mutacion_horizontal += 1
                    self.mutacion = True
                    print(f"Mutación horizontal encontrada en la fila {i+1} posición {j}-{j+3}")
                    break  # Sale si encuentra la primera mutación de la fila

    def detectar_mutantes_vertical(self):
        for j in range(len(self.adn_list[0])):
            for i in range(len(self.adn_list) - 3):  # Verificar 4 filas antes del final
            for i in range(len(self.adn_list) - 3):  # Verificar 4 filas antes del final
                if (self.adn_list[i][j] == self.adn_list[i+1][j] == self.adn_list[i+2][j] == self.adn_list[i+3][j]):
                    self.mutacion_vertical += 1
                    self.mutacion = True
                    print(f"Mutación vertical encontrada en la columna {j+1} posición {i}-{i+3}")
                    break

    def detectar_mutantes_diagonal(self):
        for i in range(len(self.adn_list) - 3):
            for j in range(len(self.adn_list[0]) - 3):  # Verificar 4 columnas antes del final
            for j in range(len(self.adn_list[0]) - 3):  # Verificar 4 columnas antes del final
                if (self.adn_list[i][j] == self.adn_list[i+1][j+1] == self.adn_list[i+2][j+2] == self.adn_list[i+3][j+3]):
                    self.mutacion_diagonal += 1
                    self.mutacion = True
                    print(f"Mutación diagonal encontrada desde ({i+1},{j+1}) hasta ({i+4},{j+4})")
                    break

    def detectar_mutantes_diagonal_inverso(self):
        for i in range(len(self.adn_list) - 3):
            for j in range(3, len(self.adn_list[0])):  # Comienza desde la columna 3 hasta el final
            for j in range(3, len(self.adn_list[0])):  # Comienza desde la columna 3 hasta el final
                if (self.adn_list[i][j] == self.adn_list[i+1][j-1] == self.adn_list[i+2][j-2] == self.adn_list[i+3][j-3]):
                    self.mutacion_diagonal += 1
                    self.mutacion = True
                    print(f"Mutación diagonal inversa encontrada desde ({i+1},{j+1}) hasta ({i+4},{j-4})")
                    break

    def analizar_mutaciones(self):
        self.detectar_mutantes_horizontal()
        self.detectar_mutantes_vertical()
        self.detectar_mutantes_diagonal()
        self.detectar_mutantes_diagonal_inverso()
        print("Análisis completado.")

    def resumen(self): 
        print(f"Hay mutacion?: {self.mutacion}")
        print(f"Número de mutaciones horizontales: {self.mutacion_horizontal}")
        print(f"Número de mutaciones verticales: {self.mutacion_vertical}")
        print(f"Número de mutaciones en diagonales: {self.mutacion_diagonal}")

class Mutador: # Clase encargada de ver que tipo de mutacion quiere agregar
class Mutador: # Clase encargada de ver que tipo de mutacion quiere agregar
    __Saludar="Bienvenido al Mutador de ADN"
    def __init__(self, adn_list:list):
        self.base_nitrogenada = ("A", "G", "T", "C")
        self.adn_list = adn_list
        self.posicion_horizontal = 0
        self.posicion_vertical = 0
        
    def Saludo(self):
        print(self.__Saludar)
        try:
            while True:
                print("""
            ¿Que tipo de mutacion desea realizar?
            1) Radiacion
            2) Virus
            0) Volver al menu principal
                """)
                muto = str(input())
                if muto == "1":
                    return 1  # Retorna 1 al elegir radiación
                elif muto == "2":
                    return 2  # Retorna 2 al elegir virus
                elif muto == "0":
                    print("Volviendo al programa principal...")
                    print("Volviendo al programa principal...")
                    return 0  # Retorna 0 si quiere volver al menú principal
                else:
                    print("Elija una opción en pantalla.")
        except IndexError:
            print("Primero debe ingresar el ADN")

    def crear_mutante(self):
        pass



class Radiacion(Mutador): # Clase encargada de añadir mutaciones horizontales y verticales
class Radiacion(Mutador): # Clase encargada de añadir mutaciones horizontales y verticales
    def __init__(self, adn_list):
        super().__init__(adn_list)
        self.radiaciones= False
        try:
            print("Iniciando mutaciones con radiación")
            self.radiar_mutaciones()
            print(f"""ADN:
          {adn_list[0]}
          {adn_list[1]}
          {adn_list[2]}
          {adn_list[3]}
          {adn_list[4]}
          {adn_list[5]}""")  # Muestra el adn modificado
            input("Presione Enter para continuar...")
        except ValueError and IndexError:
            print("Primero debe ingresar el ADN")

    def crear_mutantes_horizontal(self):
        for posicion_vertical in range(len(self.adn_list)): # Si encuentra posibles mutaciones las genera
        for posicion_vertical in range(len(self.adn_list)): # Si encuentra posibles mutaciones las genera
            cadena = self.adn_list[posicion_vertical]
            for posicion_horizontal in range(len(cadena) - 3):
                if cadena[posicion_horizontal] == cadena[posicion_horizontal+1] == cadena[posicion_horizontal+2]:
                    cadena[posicion_horizontal+3] = cadena[posicion_horizontal]
                    self.radiaciones= True
                    break
            if cadena[posicion_horizontal+3] == cadena[posicion_horizontal+2] == cadena[posicion_horizontal+1]:
                    cadena[posicion_horizontal] = cadena[posicion_horizontal+3]
                    self.radiaciones= True
        if self.radiaciones == False: # Si no encuentra posibles mutaciones genera una aleatorea
        if self.radiaciones == False: # Si no encuentra posibles mutaciones genera una aleatorea
            posicion_vertical = random.randint(0, len(self.adn_list))
            posicion_horizontal = random.randint(0, len(self.adn_list[0]) - 3)
            base=random.choice(self.base_nitrogenada)
            for posicion_horizontal in range(len(self.adn_list) - 2):
                self.adn_list[posicion_vertical][posicion_horizontal] = base
            
    def crear_mutantes_vertical(self):
        for posicion_horizontal in range(len(self.adn_list[0])): # Si encuentra posibles mutaciones las genera
        for posicion_horizontal in range(len(self.adn_list[0])): # Si encuentra posibles mutaciones las genera
            for posicion_vertical in range(len(self.adn_list) - 3):
                if (self.adn_list[posicion_vertical][posicion_horizontal] == self.adn_list[posicion_vertical+1][posicion_horizontal] ==self.adn_list[posicion_vertical+2][posicion_horizontal]):
                    self.adn_list[posicion_vertical+3][posicion_horizontal] = self.adn_list[posicion_vertical][posicion_horizontal]
                    self.radiaciones= True
                    break
            if (self.adn_list[posicion_vertical+3][posicion_horizontal] == self.adn_list[posicion_vertical+2][posicion_horizontal] ==self.adn_list[posicion_vertical+1][posicion_horizontal]):
                self.adn_list[posicion_vertical][posicion_horizontal] = self.adn_list[posicion_vertical+3][posicion_horizontal]
                self.radiaciones= True
        if self.radiaciones == False: # Si no encuentra posibles mutaciones genera una aleatorea
        if self.radiaciones == False: # Si no encuentra posibles mutaciones genera una aleatorea
            posicion_vertical = random.randint(0, len(self.adn_list) - 3)
            posicion_horizontal = random.randint(0, len(self.adn_list[0]))
            base=random.choice(self.base_nitrogenada)
            for posicion_vertical in range(len(self.adn_list) - 2):
                self.adn_list[posicion_vertical][posicion_horizontal] = base

    def radiar_mutaciones(self):
        self.crear_mutantes_horizontal()
        self.crear_mutantes_vertical()
        print("Mutaciones completadas.")



class Virus(Mutador):
    def __init__(self, adn_list):
        super().__init__(adn_list)
        self.viruses= False
        try:
            print("Iniciando mutaciones con virus")
            self.virus_mutaciones()
            print(f"""ADN:
          {adn_list[0]}
          {adn_list[1]}
          {adn_list[2]}
          {adn_list[3]}
          {adn_list[4]}
          {adn_list[5]}""")  # Muestra el adn modificado
            input("Presione Enter para continuar...")
        except IndexError and ValueError:
            print("Primero debe ingresar el ADN")
     
    def crear_mutantes_diagonal(self):
        for self.posicion_vertical in range(len(self.adn_list) - 3): # Si encuentra posibles mutaciones las genera
            for self.posicion_horizontal in range(len(self.adn_list[0]) - 3):
        for self.posicion_vertical in range(len(self.adn_list) - 3): # Si encuentra posibles mutaciones las genera
            for self.posicion_horizontal in range(len(self.adn_list[0]) - 3):
                if (self.adn_list[self.posicion_vertical][self.posicion_horizontal] == self.adn_list[self.posicion_vertical+1][self.posicion_horizontal+1] == self.adn_list[self.posicion_vertical+2][self.posicion_horizontal+2]):
                    self.adn_list[self.posicion_vertical+3][self.posicion_horizontal+3] = self.adn_list[self.posicion_vertical][self.posicion_horizontal]
                    self.viruses= True
                    break
            if (self.adn_list[self.posicion_vertical+3][self.posicion_horizontal+3] == self.adn_list[self.posicion_vertical+2][self.posicion_horizontal+2] == self.adn_list[self.posicion_vertical+1][self.posicion_horizontal+1]):
                    self.adn_list[self.posicion_vertical][self.posicion_horizontal] = self.adn_list[self.posicion_vertical+3][self.posicion_horizontal+3]
                    self.viruses= True
        if self.viruses == False: # Si no encuentra posibles mutaciones genera una aleatorea
        if self.viruses == False: # Si no encuentra posibles mutaciones genera una aleatorea
            posicion_vertical = random.randint(0, len(self.adn_list) - 4)
            posicion_horizontal = random.randint(0, len(self.adn_list[0]) - 4)
            base=random.choice(self.base_nitrogenada)
            for i in range(4):  
            for i in range(4):  
                if (posicion_vertical + i < len(self.adn_list) and 
                        posicion_horizontal + i < len(self.adn_list[0])):
                    self.adn_list[posicion_vertical + i][posicion_horizontal + i] = base

    def crear_mutantes_diagonal_inverso(self):
        for self.posicion_vertical in range(len(self.adn_list) - 3): # Si encuentra posibles mutaciones las genera
            for self.posicion_horizontal in range(3, len(self.adn_list[0])):  
        for self.posicion_vertical in range(len(self.adn_list) - 3): # Si encuentra posibles mutaciones las genera
            for self.posicion_horizontal in range(3, len(self.adn_list[0])):  
                if (self.adn_list[self.posicion_vertical][self.posicion_horizontal] == self.adn_list[self.posicion_vertical+1][self.posicion_horizontal-1] == self.adn_list[self.posicion_vertical+2][self.posicion_horizontal-2]):
                    self.adn_list[self.posicion_vertical+3][self.posicion_horizontal-3] = self.adn_list[self.posicion_vertical][self.posicion_horizontal]
                    self.viruses= True
                    break
            if (self.adn_list[self.posicion_vertical+3][self.posicion_horizontal-3] == self.adn_list[self.posicion_vertical+2][self.posicion_horizontal-2] == self.adn_list[self.posicion_vertical+1][self.posicion_horizontal-1]):
                    self.adn_list[self.posicion_vertical][self.posicion_horizontal] = self.adn_list[self.posicion_vertical+3][self.posicion_horizontal-3]
                    self.viruses= True
        if self.viruses == False: # Si no encuentra posibles mutaciones genera una aleatorea
        if self.viruses == False: # Si no encuentra posibles mutaciones genera una aleatorea
            posicion_vertical = random.randint(3, len(self.adn_list) - 1)
            posicion_horizontal = random.randint(3, len(self.adn_list[0]) - 1)
            base=random.choice(self.base_nitrogenada)
            for i in range(4): 
            for i in range(4): 
                if (posicion_vertical - i >= 0 and 
                        posicion_horizontal - i >= 0):
                    self.adn_list[posicion_vertical - i][posicion_horizontal - i] = base

    def virus_mutaciones(self):
        self.crear_mutantes_diagonal()
        self.crear_mutantes_diagonal_inverso()
        print("Mutaciones completadas.")

class Sanador: # Clase encargada de Sanar el adn
class Sanador: # Clase encargada de Sanar el adn
    SaludarS= "Bienvenido al Sanador de Mutaciones"
    def __init__(self, adn_list):
        try:
            self.base_nitrogenada = ("A", "G", "T", "C")
            self.adn_list = adn_list
            self.mutacion = False
            self.analizar_mutaciones()  # Llama a los métodos de análisis
            self.analizar_mutaciones()  # Llama a los métodos de análisis
        except IndexError:
            print("Primero debe ingresar el ADN")

    def detectar_mutantes_horizontal(self):
        for i in range(len(self.adn_list)):
            cadena = self.adn_list[i]
            for j in range(len(cadena) - 3):  # Verificar 4 caracteres antes del final
            for j in range(len(cadena) - 3):  # Verificar 4 caracteres antes del final
                if cadena[j] == cadena[j+1] == cadena[j+2] == cadena[j+3]:
                    self.mutacion = True
                    break  # Sale si encuentra la primera mutación en la fila
                    break  # Sale si encuentra la primera mutación en la fila

    def detectar_mutantes_vertical(self):
        for j in range(len(self.adn_list[0])):
            for i in range(len(self.adn_list) - 3):  # Verificar 4 filas antes del final
            for i in range(len(self.adn_list) - 3):  # Verificar 4 filas antes del final
                if (self.adn_list[i][j] == self.adn_list[i+1][j] == self.adn_list[i+2][j] == self.adn_list[i+3][j]):
                    self.mutacion = True
                    break

    def detectar_mutantes_diagonal(self):
        for i in range(len(self.adn_list) - 3):
            for j in range(len(self.adn_list[0]) - 3):  # Verificar 4 columnas antes del final
            for j in range(len(self.adn_list[0]) - 3):  # Verificar 4 columnas antes del final
                if (self.adn_list[i][j] == self.adn_list[i+1][j+1] == self.adn_list[i+2][j+2] == self.adn_list[i+3][j+3]):
                    self.mutacion = True
                    break

    def detectar_mutantes_diagonal_inverso(self):
        for i in range(len(self.adn_list) - 3):
            for j in range(3, len(self.adn_list[0])):  # Comienza desde la columna 3 hasta el final
            for j in range(3, len(self.adn_list[0])):  # Comienza desde la columna 3 hasta el final
                if (self.adn_list[i][j] == self.adn_list[i+1][j-1] == self.adn_list[i+2][j-2] == self.adn_list[i+3][j-3]):
                    self.mutacion = True
                    break

    def generar_lista_random(self):
        # Genera una matriz 6x6 con letras aleatorias de self.base_nitrogenada
        self.adn_list = [[random.choice(self.base_nitrogenada) for _ in range(6)] for _ in range(6)]

    def analizar_mutaciones(self):
        while True:
            self.mutacion = False  # Reinicia mutación
            self.mutacion = False  # Reinicia mutación
            self.detectar_mutantes_horizontal()
            self.detectar_mutantes_vertical()
            self.detectar_mutantes_diagonal()
            self.detectar_mutantes_diagonal_inverso()
            if self.mutacion:
                self.generar_lista_random()  # Genera una nueva lista si hay mutación
            else:
                break  # Sale del bucle si no hay mutación
        # Imprime el adn nuevo si no se detectaron mutaciones
        # Imprime el adn nuevo si no se detectaron mutaciones
        print(f"""ADN:
      {self.adn_list[0]}
      {self.adn_list[1]}
      {self.adn_list[2]}
      {self.adn_list[3]}
      {self.adn_list[4]}
      {self.adn_list[5]}""")
        print("Sanador completado.")
        input("Presione Enter para continuar...")
        return self.adn_list