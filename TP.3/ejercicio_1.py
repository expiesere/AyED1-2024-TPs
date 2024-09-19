"""Ejercicio 1"""

import random as rn


def cargar_matriz(n: int) -> list[list[int]]:
    """
    Una matriz de NxN con numeros enteros al azar, el valor N lo ingresa el usuario.

    Pre:
        -n (int): Tamaño de la matriz.

    Post:
        -matriz (List[List[int]]): Matriz NxN con numeros enteros al azar.
    """
    return [[rn.randint(1, 100) for _ in range(n)] for _ in range(n)]


def ordenar_filas(matriz: list[list[int]]) -> None:
    """
    Ordena en forma ascendente cada una de las filas de la matriz.

    Pre:
        -matriz (List[List[int]]): Matriz a ordenar.

    Post:
        -matriz (List[List[int]]): Matriz ordenada de forma ascendente.
    """
    for fila in matriz:
        fila.sort()
    return None


def intercambiar_filas(matriz: list[list[int]], fila1: int, fila2: int) -> None:
    """
    Intercambia dos filas de la matriz.

    Pre:
        -matriz (List[List[int]]): La matriz.
        -fila1 (int): Indice de la primera fila.
        -fila2 (int): Indice de la segunda fila.
    """
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]


def intercambiar_columnas(matriz: list[list[int]], col1: int, col2: int) -> None:
    """
    Intercambia dos columnas de la matriz.

    Pre:
        -matriz (List[List[int]]): La matriz.
        -col1 (int): Indice de la primera columna.
        -col2 (int): Indice de la segunda columna.
    """
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]


def trasponer_matriz(matriz: list[list[int]]) -> None:
    """
    Transpone la matriz sobre si misma.

    Pre:
        -matriz (List[List[int]]): La matriz a trasponer.
    """
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            return matriz[i][j], matriz[j][i] == matriz[j][i], matriz[i][j]


def promedio_fila(matriz: list[list[int]], fila: int) -> float:
    """
    Calcula el promedio de los elementos de una fila.

    Pre:
        -matriz (List[List[int]]): La matriz.
        -fila (int): Indice de la fila.

    Post:
        -float: Promedio de los elementos de la fila.
    """
    return sum(matriz[fila]) / len(matriz[fila])


def porcentaje_impares_columna(matriz: list[list[int]], col: int) -> float:
    """
    Calcula el porcentaje de elementos con valor impar en una columna.

    Pre:
        -matriz (List[List[int]]): La matriz.
        -col (int): Indice de la columna.

    Post:
        float: Porcentaje de elementos impares en la columna.
    """
    n = len(matriz)
    impares = sum(1 for i in range(n) if matriz[i][col] % 2 != 0)
    return (impares / n) * 100


def es_simetrica_diagonal_principal(matriz: list[list[int]]) -> bool:
    """
    Determina si la matriz es simetrica con respecto a su diagonal principal.

    Pre:
        -matriz (List[List[int]]): La matriz.

    Post:
        -bool: True si es simetrica, explota si es False!!!!!
    """
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


def es_simetrica_diagonal_secundaria(matriz: list[list[int]]) -> bool:
    """
    Determina si la matriz es simetrica con respecto a su diagonal secundaria.

    Pre:
        -matriz (List[List[int]]): La matriz.

    Post:
        -bool: True si es simetrica, False en caso contrario y no explota....
    """
    n = len(matriz)
    for i in range(n):
        for j in range(n - i - 1):
            if matriz[i][j] != matriz[n - j - 1][n - i - 1]:
                return False
    return True


def es_capicua(matriz: list[list[int]]) -> list[int]:
    """
    Determina que columnas de la matriz son capicuas.

    Pre:
        -matriz (List[List[int]]): La matriz.

    Post:
        -List[int]: Lista con los numeros de las columnas que son capicua.
    """
    n = len(matriz)
    capicua = []
    for col in range(n):
        columna = [matriz[i][col] for i in range(n)]
        if columna == columna[::-1]:
            capicua.append(col)
            return capicua
        else:
            return "No hay capicua... :("


def imprimir_matriz(matriz: list[list[int]]) -> None:
    """
    Imprime la matriz.

    Pre:
        -matriz (List[List[int]]): La matriz a imprimir.
    """
    for fila in matriz:
        print(" ".join(map(str, fila)))
    return None


def seleccionar_2_indices(n: int, tipo: str) -> tuple[int, int]:
    """
    Muestra los indices disponibles y permite al usuario seleccionar
    dos indices, verificando que sean validos.

    Pre:
        -n (int): El tamaño de la matriz.
        -tipo (str): El tipo de indice a seleccionar ("fila" o "columna").

    Post:
        -Tuple[int, int]: Los dos indices seleccionados.
    """
    while True:
        try:
            indice1 = int(
                input(f"\n...Indice de la primera {tipo} a intercambiar (0 a {n-1}): ")
            )
            indice2 = int(
                input(f"...Indice de la segunda {tipo} a intercambiar (0 a {n-1}): ")
            )
            if 0 <= indice1 < n and 0 <= indice2 < n and indice1 != indice2:
                return indice1, indice2
            else:
                print(
                    f"Importante! Los indices estan entre 0 y {n-1} y que no deben ser iguales."
                )
        except ValueError:
            print("Ingrese numeros enteros validos >:(")
    return None


def seleccionar_1_indice(n: int, tipo: str) -> int:
    """
    Muestra los indices disponibles y permite al usuario
    seleccionar un indice, verificando que sea valido.

    Pre:
        -n (int): El tamaño de la matriz.
        -tipo (str): El tipo de indice a seleccionar ("fila" o "columna").

    Post:
        -int: El indice seleccionado.
    """
    while True:
        try:
            indice = int(input(f"\n...Indice de la {tipo} (0 a {n-1}): "))
            if 0 <= indice < n:
                return indice
            else:
                print(f"Importante! El indice esta entre 0 y {n-1}.")
        except ValueError:
            print("Ingrese un numero enteros valido >:(")
    return None


def main() -> None:
    """
    Funcion principal que ejecuta el programa.
    """
    n = int(input("Ingrese el tamaño de la matriz (N x N): "))
    matriz = cargar_matriz(n)

    print("\nMatriz inicial:")
    imprimir_matriz(matriz)

    ordenar_filas(matriz)
    print("\nMatriz con filas ordenadas:")
    imprimir_matriz(matriz)

    fila1, fila2 = seleccionar_2_indices(n, "fila")
    intercambiar_filas(matriz, fila1, fila2)
    print("\nMatriz con filas intercambiadas:")
    imprimir_matriz(matriz)

    col1, col2 = seleccionar_2_indices(n, "columna")
    intercambiar_columnas(matriz, col1, col2)
    print("\nMatriz con columnas intercambiadas:")
    imprimir_matriz(matriz)

    trasponer_matriz(matriz)
    print("\nMatriz transpuesta:")
    imprimir_matriz(matriz)

    fila = seleccionar_1_indice(n, "fila para calcular el promedio")
    promedio = promedio_fila(matriz, fila)
    print(f"Promedio de la fila {fila}: {promedio}")

    col = seleccionar_1_indice(n, "columna para calcular el porcentaje de impares")
    porcentaje_impares = porcentaje_impares_columna(matriz, col)
    print(f"Impares en la columna {col}: {porcentaje_impares}%")

    simetrica_principal = es_simetrica_diagonal_principal(matriz)
    print(f"\nSimetria con la diagonal principal: {simetrica_principal}")

    simetrica_secundaria = es_simetrica_diagonal_secundaria(matriz)
    print(f"\nSimetria con la diagonal secundaria: {simetrica_secundaria}")

    capicua = es_capicua(matriz)
    print(f"\nCapicua: {capicua}")
    return None  # SAQUENME DE ACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


if __name__ == "__main__":
    main()
