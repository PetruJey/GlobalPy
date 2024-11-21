def guia():
    #Muestra en pantalla una guía para ingresar los datos del ADN.
    print("""
    -La secuencia del ADN se ingresa de izquierda a derecha.
    -El ADN elegido se ingresa por filas (con 6 bases nitrogenadas por fila.).
      A G A T C A - Fila 1
      G A T T C A - Fila 2
      C A A C A T - Fila 3
      G A G C T A - Fila 4
      A T T G C G - Fila 5
      C T G T T C - Fila 6
          """)
    input("Presione Enter para continuar...")
    
def verificar_adn(value):
    bases_nitrogenadas = ("A", "G", "T", "C") 
    if len(value) != 6:  
        print("Error: La fila debe contener 6 bases nitrogenadas.")
        return False

    for base in value:  
        if base not in bases_nitrogenadas:
            print("Error: Tiene que ingresar únicamente bases nitrogenadas.")
            return False
            
    return True 
    
def ingresar_adn(adn):
    i = 0
    posiciones_list = ("la primera", "la segunda", "la tercera", "la cuarta", "la quinta", "la sexta")
    if not adn:
        while i < 6:
            value = input(f"Ingrese {posiciones_list[i]} fila de su ADN: ")
            value = value.upper()
            if verificar_adn(value):
                adn.append(list(value))  # Guardar como lista de caracteres
                i += 1
            else:
                print("Fila inválida, Ingrese de nuevo.")
    else:
        example = str(input("Ya existe un ADN guardado, desea borrarlo?\n1 - Si\n2 - No\n"))
        if example == "1":
            adn.clear()
        else:
            print("Volviendo al Menu...")
    try:
        print(f"""ADN:
          {adn[0]}
          {adn[1]}
          {adn[2]}
          {adn[3]}
          {adn[4]}
          {adn[5]}""")
    except IndexError:
        print(f"ADN", adn)
    input("Presione Enter para continuar...")
