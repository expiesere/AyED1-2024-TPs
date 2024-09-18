"""Ejercicio 2"""

import random as rn


def cargar_matriz(n: int) -> list:
    """
    Carga una matriz de tamaño NxN con numeros al azar.

    Pre:
        -n (int): El numero de filas y columnas que tiene la matriz.

    Post:
        -X[NxN[int]]: Matrices con numeros al azar.
    """
    return [[rn.randint(1, 100) for _ in range(n)] for _ in range(n)]


def main() -> None:
    """
    Le solicita al usuario una cantidad de matrices y sus tamaños,
    luego invoca la funcion cargar_matriz para rellenarlas.
    """
    x = int(input("Cantidad de matrices a generar: "))
    n = int(input("Tamaño de matrices: "))
    for i in range(x):
        matriz = cargar_matriz(n)
        print(f"\nMATRIZ N°{i+1}")
        for fila in matriz:
            print(" ".join(map(str, fila)))
        print()
    return None


if __name__ == "__main__":
    main()
