"""Ejercicio 3"""
import os

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def cargar_matriz(n: int) -> list:
    """Genera una matriz de tamaño NxN con numeros enteros unicos en
    intervalos de [0, N^2).

    Pre:
        -n (int): El numero de filas y columnas que tiene la matriz.

    Post:
        list[NxN[int]]: Matriz NxN con numeros enteros unicos.
    """
    numeros = list(range(n * n))  # :O
    matriz = [numeros[i * n : (i + 1) * n] for i in range(n)]
    return matriz


def main() -> None:
    """
    Funcion principal que ejecuta las demas funciones.

    No retorna nada.
    """
    clear_screen()
    n = int(input("Ingrese el tamaño de la matriz (N x N): "))
    matriz = cargar_matriz(n)
    print("\nMATRIZ: ")
    for fila in matriz:
        print(" ".join(map(str, fila)))
    return None


if __name__ == "__main__":
    main()
