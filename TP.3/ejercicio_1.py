"""Ejercicio 1"""

def opciones():
    """Imprime las opciones"""
    print("\nMENU PRINCIPAL")
    print("1- Cargar matriz")
    print("2- Ordenar los elementos de las filas de forma ascendente")
    print("3- Intercambiar dos filas")
    print("4- Intercambiar dos columnas")
    print("5- Trasponer fila sobre si misma")
    print("6- Promedio de elementos de una fila")
    print("7- Porcentaje de elementos impares de una columna")
    print("8- Simetria con su diagonal principal")
    print("9- Simetria con su diagonal secundaria")
    print("10- Capicua con columnas")
    print("11- Salir del programa")
    return None

def cargar_matriz(n):
    """
    Carga una matriz de tamaño NxN con numeros enteros ingresados por el usuario.

    Pre:
        -n (int): Tamaño de la matriz, es el numero de filas y columnas

    Post:
        -list: Matriz NxN con los numeros ingresados
    """
    matriz = []
    for i in range(n):
        fila = list(
            map(
                int,
                input(
                    f"Ingrese los elementos de la fila {i+1} separados por espacios: "
                ).split(),
            )
        )
        matriz.append(fila)
    return matriz


def ordenar_filas(matriz):
    """
    Ordena en forma ascendente cada una de las filas de la matriz.

    Pre:
        -Matriz a ordenar

    Post:
        -Matriz con las filas ordenadas
    """
    for i in range(len(matriz)):
        matriz[i].sort()
    return matriz


def intercambiar_filas(matriz, fila1, fila2):
    """Intercambia dos filas de la matriz.
    
    Pre:
        -Matriz en la que se intercambiaran las filas 
        -fila1 (int), indice de la primer fila
        -fila2 (int), indice de la segunda fila

    Post:
        -Matriz con las filas intercambiadas
    
    """
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
    return matriz


def intercambiar_columnas(matriz, col1, col2):
    """
    Intercambia dos columnas de la matriz.

    Pre:
        -Matriz en la que se intercambiaran las columnas
        -col1 (int), indice de la primera columna
        -col2 (int), indice de la segunda columna

    Post:
        -Matriz con las columnas intercambiadas
    """
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]
    return matriz


def trasponer_matriz(matriz):
    """
    Intercambia la matriz sobre si misma

    Pre:
        -Matriz a intercambiar
    
    Post:
        -Matriz intercambiada
    """
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    return matriz


def promedio_fila(matriz, fila):
    """Calcula el promedio de los elementos de una fila.
    
    Pre:
        -Matriz en la que se calcula el promedio
        -Indice de la fila

    Post:
        -Promedio de los elementos de la fila
    """
    return sum(matriz[fila]) / len(matriz[fila])


def imprimir_matriz(matriz):
    """Imprime la matriz"""
    for fila in matriz:
        print(" ".join(map(str, fila)))
    return None


def main():
    """Funcion principal"""
    while True:
        opciones()
        op = input("...Seleccione una opcion: ")

        match op:
            case "1":
                n = int(input("\nIngrese el tamaño de la matriz: "))
                matriz = cargar_matriz(n)
                print("\nMATRIZ: ")
                imprimir_matriz(matriz)
            case "2":
                matriz = ordenar_filas(matriz)
                print("\nFILAS ORDENADAS:")
                imprimir_matriz(matriz)
            case "3":
                fila1, fila2 = map(int,input("Ingrese las dos filas a intercambiar separadas por un espacio: ").split(),)
                matriz = intercambiar_filas(matriz, fila1, fila2)
                print("\nFILAS INTERCAMBIADAS:")
                imprimir_matriz(matriz)
            case "4":
                col1, col2 = map(int,input("Ingrese las dos columnas a intercambiar separadas por un espacio: ").split(),)
                matriz = intercambiar_columnas(matriz, col1, col2)
                print("\nCOLUMNAS INTERCAMBIADAS:")
                imprimir_matriz(matriz)
            case "5":
                matriz = trasponer_matriz(matriz)
                print("\nMATRIZ TRASPUESTA:")
                imprimir_matriz(matriz)
            case "6":
                fila = int(input("Ingrese el numero de la fila para calcular el promedio: "))
                promedio = promedio_fila(matriz, fila)
                print(f"\nPROMEDIO DE LA FILA {fila}: {promedio}")
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass
            case "10":
                pass
            case "11":
                print("\nAdios!")
                break
            case _:
                print("\n...Opcion incorrecta, intente de nuevo.")
    return None

if __name__ == "__main__":
    main()
