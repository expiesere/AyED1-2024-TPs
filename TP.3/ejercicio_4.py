"""Ejercicio 4"""

import random as rn


def generar_matriz_produccion(n: int) -> list[list[int]]:
    """
    Genera una matriz de tamaño N x 7-dias de la semana con
    numeros enteros al azar en el intervalo [0, 150].

    Pre:
        -n (int): El numero de fábricas.

    Post:
        -list[List[int]]: Matriz Nx7 con la cantidad de bicicletas producidas
    """
    return [[rn.randint(0, 150) for _ in range(7)] for _ in range(n)]


def total_por_fabrica(matriz: list[list[int]]) -> list[int]:
    """
    Calcula el total de bicicletas fabricadas por cada fabrica.

    Pre:
        -matriz (List[List[int]]): Matriz de produccion.

    Post:
        -List[int]: Lista con el total de bicicletas fabricadas por cada fabrica.
    """
    return [sum(fila) for fila in matriz]


def fabrica_max_produccion(matriz: list[list[int]]) -> tuple[int, int, int]:
    """
    Encuentra la fabrica que mas produjo en un solo dia.

    Pre:
        -matriz (List[List[int]]): Matriz de produccion.

    Post:
        -Tuple[int, int, int]: Fabrica, dia y cantidad maxima producida.
    """
    max_produccion = 0
    fabrica = -1
    dia = -1
    for i, fila in enumerate(matriz):
        for j, produccion in enumerate(fila):
            if produccion > max_produccion:
                max_produccion = produccion
                fabrica = i
                dia = j
    return fabrica, dia, max_produccion


def dia_mas_productivo(matriz: list[list[int]]) -> int:
    """
    Encuentra el dia mas productivo considerando todas las fabricas combinadas.

    Pre:
        -matriz (List[List[int]]): Matriz de produccion.

    Post:
        -int: Dia mas productivo.
    """
    produccion_por_dia = [
        sum(matriz[i][j] for i in range(len(matriz))) for j in range(7)
    ]
    return produccion_por_dia.index(max(produccion_por_dia))


def menor_produccion_por_fabrica(matriz: list[list[int]]) -> list[int]:
    """
    Crea una lista por comprension que contenga la menor cantidad fabricada por cada fabrica.

    Pre:
        -matriz (List[List[int]]): Matriz de produccion.

    Post:
        -List[int]: Lista con la menor cantidad fabricada por cada fabrica.
    """
    return [min(fila) for fila in matriz]


def main() -> None:
    """
    Funcion principal que ejecuta el programa.
    """
    n = int(input("Ingrese el numero de fabricas: "))
    matriz = generar_matriz_produccion(n)

    print("\nMatriz de produccion:")
    for fila in matriz:
        print(" ".join(map(str, fila)))

    print("\nTotal de bicicletas fabricadas por cada fabrica:")
    totales = total_por_fabrica(matriz)
    for i, total in enumerate(totales):
        print(f"Fabrica {i+1}: {total} bicicletas")

    fabrica, dia, max_produccion = fabrica_max_produccion(matriz)
    print(
        f"\nLa fabrica que mas produjo en un solo dia fue la fabrica {fabrica+1} en el dia {dia+1} con {max_produccion} bicicletas."
    )

    dia_productivo = dia_mas_productivo(matriz)
    print(f"\nEl dia mas productivo fue el dia {dia_productivo+1}.")

    menores = menor_produccion_por_fabrica(matriz)
    print("\nMenor cantidad fabricada por cada fabrica:")
    for i, menor in enumerate(menores):
        print(f"Fabrica {i+1}: {menor} bicicletas")
    return None


if __name__ == "__main__":
    main()
