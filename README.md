**ADN Project Python**
======================
Este programa evalúa secuencias de ADN organizadas en una matriz de 6x6 para identificar mutaciones y brinda la posibilidad de modificarlas (mutarlas) o sanarlas. Su atención se centra en las bases nitrogenadas del ADN: 
- Adenina (A)
- Timina (T)
- Citosina (C)
- Guanina (G).
<p align = "center">
<img src="https://cdn.icon-icons.com/icons2/609/PNG/512/dna_icon-icons.com_56352.png" width="200" height="300" />

> ### Integrantes - Comisión 3
> - Jeremias Montiel
> - Pablo Vivas
> - Bruno Racconto

### Instrucciones
**1** - Se ejecuta el archivo "ejecutable.py".
**2** - Una vez inicializado se mostrará en pantalla un menú del cual se ingresará la opción deseada numéricamente.

```
    **Menú principal**
        1) Guía
        2) Ingresar ADN
        3) Detector de Mutaciones
        4) Mutador
        5) Sanador
        0) Salir del programa
```
***
####  **1) Guía**
- Presionando la tecla **"1"** se ilustrará un paso a paso de cómo introducir una secuencia de ADN.
```
	-La secuencia del ADN se ingresa de izquierda a derecha.
	-El ADN elegido se ingresa por filas (con 6 bases nitrogenadas por fila.).
	A G A T C A - Fila 1
	G A T T C A - Fila 2
	C A A C A T - Fila 3
	G A G C T A - Fila 4
	A T T G C G - Fila 5
	C T G T T C - Fila 6

	Presione una Enter para continuar...
```
***
#### **2) Ingresar ADN**
- Presionando la tecla **"2"** el programa solicitará la secuencia de ADN del Usuario, para ser ingresada fila por fila, la cual se mostrará en pantalla al finalizar el ingreso de la misma.
```
Ingrese la primera fila de su ADN: actgca
Ingrese la segunda fila de su ADN: tagcta
Ingrese la tercera fila de su ADN: gtacga
Ingrese la cuarta fila de su ADN: tagcta
Ingrese la quinta fila de su ADN: taccgt
Ingrese la sexta fila de su ADN: tgtcta
ADN:
          ['A', 'C', 'T', 'G', 'C', 'A']
          ['T', 'A', 'G', 'C', 'T', 'A']
          ['G', 'T', 'A', 'C', 'G', 'A']
          ['T', 'A', 'G', 'C', 'T', 'A']
          ['T', 'A', 'C', 'C', 'G', 'T']
          ['T', 'G', 'T', 'C', 'T', 'A']
Presione Enter para continuar...
```
***
#### **3) Detector de Mutaciones**
- Presionando la tecla **"3"** se iniciará el proceso de detección de mutaciones, cuyo proceso analizará si se halla una mutación de manera Horizontal, Vertical o Diagonal, e indicará su ubicación en la matriz.
```
Analizando ADN...
Mutación vertical encontrada en la columna 3 posición 1-4
Mutación vertical encontrada en la columna 5 posición 0-3
Análisis completado.
Hay mutacion?: True
Número de mutaciones horizontales: 0
Número de mutaciones verticales: 2
Número de mutaciones en diagonales: 0
Presione Enter para continuar...
```
***





