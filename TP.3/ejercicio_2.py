"""Ejercicio 2"""

import random as rn
import os
from typing import List


def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


def matriz_a(n: int) -> List[List[int]]:
    """
    Genera una matriz de tamaño ( N ) con numeros 
    impares en la diagonal principal.

    Pre:
        -n(int): Valor N que ingresa el usuario para determinar el
        tamaño de la matriz.

    Post:
        -List[List[int]]: Matriz de numeros impares en la
    diagonal principal.
    """
    matriz = [[0 for i in range(n)] for i in range(n)]
    numero_impar = 1
    for i in range(n):
        matriz[i][i] = numero_impar
        numero_impar += 2
    return matriz


def matriz_b(n: int) -> List[List[int]]:
    """
    Genera una matriz de tamaño ( N ) con 
    potencias de 3 en la diagonal secundaria.

    Pre:
        -n(int): Valor N que ingresa el usuario para determinar el
        tamaño de la matriz.

    Post:
        -List[List[int]]: Matriz con numeros de potencia de 3
        en la diagonal secundaria.
    """
    matriz = [[0] * n for i in range(n)]
    num = 1
    for i in range(n - 1, -1, -1):
        matriz[i][n - i - 1] = num
        num *= 3
    return matriz


def matriz_c(n: int) -> List[List[int]]:
    """
    Genera una matriz de tamaño ( N ) con numeros 
    decrecientes desde ( n-i ) hasta 1.

    Pre:
        -n(int): Valor N que ingresa el usuario para determinar el
        tamaño de la matriz.

    Post:
        -List[List[int]]: Matriz con numeros decrecientes hasta 1.
    """
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        num = n - i
        for j in range(i + 1):
            matriz[i][j] = num
    return matriz


def matriz_d(n: int) -> List[List[int]]:
    """
    Genera una matriz de tamaño ( N ) con un valor inicial 
    aleatorio dividido por potencias de 2 en cada fila.

    Pre:
        -n(int): Valor N que ingresa el usuario para determinar el
        tamaño de la matriz.

    Post:
        -List[List[int]]: Matriz con numeros aleatorios divididos 
        en potencias de 2 por cada fila.
    """
    matriz = []
    valor_inicial = rn.randint(1, 100)
    for i in range(n):
        fila = [valor_inicial // (2**i)] * n
        matriz.append(fila)
    return matriz


def matriz_e(n: int) -> List[List[int]]:
    """
    Genera una matriz de tamaño ( N ) con numeros 
    consecutivos en las diagonales.

    Pre:
        -n(int): Valor N que ingresa el usuario para determinar el
        tamaño de la matriz.

    Post:
        -List[List[int]]: Matriz con numeros consecutivos en las diagonales.
    """
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    for diag in range(2 * n - 1):
        if diag % 2 == 0:
            for i in range(max(0, diag - n + 1), min(n, diag + 1)):
                j = diag - i
                matriz[i][j] = num
                num += 1
    return matriz


def matriz_f(n: int) -> List[List[int]]:
    pass


def matriz_g(n: int) -> List[List[int]]:
    """
    Genera una matriz de tamaño ( N ) con numeros 
    consecutivos en espiral.

    Pre:
        -n(int): Valor N que ingresa el usuario para determinar el
        tamaño de la matriz.

    Post:
        -List[List[int]]: Matriz con numeros consecutivos en espiral.
    """
    matriz = [[0] * n for _ in range(n)]
    num = 1
    inicio_fila, fin_fila = 0, n - 1
    inicio_col, fin_col = 0, n - 1

    while inicio_fila <= fin_fila and inicio_col <= fin_col:
        for col in range(inicio_col, fin_col + 1):
            matriz[inicio_fila][col] = num
            num += 1
        inicio_fila += 1

        for fila in range(inicio_fila, fin_fila + 1):
            matriz[fila][fin_col] = num
            num += 1
        fin_col -= 1

        if inicio_fila <= fin_fila:
            for col in range(fin_col, inicio_col - 1, -1):
                matriz[fin_fila][col] = num
                num += 1
            fin_fila -= 1

        if inicio_col <= fin_col:
            for fila in range(fin_fila, inicio_fila - 1, -1):
                matriz[fila][inicio_col] = num
                num += 1
            inicio_col += 1
    return matriz


def matriz_h(n: int) -> List[List[int]]:
    """
    Genera una matriz de tamaño ( N ) con numeros consecutivos en diagonales 
    desde la esquina superior izquierda.

    Pre:
        -n(int): Valor N que ingresa el usuario para determinar el
        tamaño de la matriz.

    Post:
        -List[List[int]]: Matriz con numeros consecutivos desde la 
        esquina superior izquierda.
    """
    matriz = [[0] * n for _ in range(n)]
    num = 1
    for i in range(2 * n - 1):
        if i < n:
            for j in range(i + 1):
                matriz[j][i - j] = num
                num += 1
        else:
            for j in range(i - n + 1, n):
                matriz[j][i - j] = num
                num += 1
    return matriz


def matriz_i(n: int) -> List[List[int]]:
    pass


def imprimir_matriz(matriz) -> None:
    """
    Imprime las matrices.
    
    No retorna nada.
    """
    for fila in matriz:
        print(" ".join(map(str, fila)))
    return None


def main() -> None:
    """
    Funcion principal que ejecuta el resto de funciones.

    No returna nada
    """
    clear_screen()
    n = int(input("Ingrese el tamaño de matriz: "))
    try:
        print("\nMATRIZ A:")
        imprimir_matriz(matriz_a(n))

        print("\nMATRIZ B:")
        imprimir_matriz(matriz_b(n))

        print("\nMATRIZ C:")
        imprimir_matriz(matriz_c(n))

        print("\nMATRIZ D:")
        imprimir_matriz(matriz_d(n))

        print("\nMATRIZ E:")
        imprimir_matriz(matriz_e(n))

        print("\nMATRIZ F:")
        print("X_X/")

        print("\nMATRIZ G:")
        imprimir_matriz(matriz_g(n))

        print("\nMATRIZ H:")
        imprimir_matriz(matriz_h(n))

        print("\nMATRIZ I:")
        print("X_X/")
    except ValueError:
        print("Error: Se debe ingresar un numero entero.")
    return None


if __name__ == "__main__":
    main()
