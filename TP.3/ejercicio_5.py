"""Ejercicio 5"""

import random as rn
import os
from typing import List, Tuple

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


def mostrar_butacas(sala: List[List[int]]) -> None:
    """
    Muestra por pantalla el estado de cada una de las butacas del cine.

    Pre:
        -sala (List[List[int]]): La matriz que representa la sala de cine.
    """
    for fila in sala:
        print(" ".join(map(str, fila)))
    return None


def reservar(sala: List[List[int]], fila: int, butaca: int) -> bool:
    """
    Reserva una butaca en la sala de cine si esta disponible.

    Pre:
        -sala (List[List[int]]): La matriz que representa la sala de cine.
        -fila (int): El indice de la fila de la butaca a reservar.
        -butaca (int): El indice de la butaca a reservar.

    Post:
        -bool: True si la butaca fue reservada, False en caso contrario.
    """
    if sala[fila][butaca] == 0:
        sala[fila][butaca] = 1
        return True
    return False


def cargar_sala(sala: List[List[int]]) -> None:
    """
    Carga la sala con valores aleatorios para simular butacas ya reservadas.

    Pre:
        -sala (List[List[int]]): La matriz que representa la sala de cine.
    """
    for i in range(len(sala)):
        for j in range(len(sala[i])):
            sala[i][j] = rn.randint(0, 1)
    return None


def butacas_libres(sala: List[List[int]]) -> int:
    """
    Retorna la cantidad de butacas desocupadas en la sala.

    Pre:
        -sala (List[List[int]]): La matriz que representa la sala de cine.

    Post:
        -int: La cantidad de butacas desocupadas.
    """
    return sum(fila.count(0) for fila in sala)


def butacas_contiguas(sala: List[List[int]]) -> Tuple[int, int, int]:
    """
    Busca la secuencia mas larga de butacas libres contiguas en una misma fila.

    Pre:
        -sala (List[List[int]]): La matriz que representa la sala de cine.

    Post:
        -Tuple[int, int, int]: Las coordenadas de inicio de la secuencia mas larga de
         butacas libres contiguas (fila, inicio, longitud).
    """
    max_fila, max_inicio, max_longitud = -1, -1, 0
    for i, fila in enumerate(sala):
        inicio, longitud = -1, 0
        for j, butaca in enumerate(fila):
            if butaca == 0:
                if inicio == -1:
                    inicio = j
                longitud += 1
            else:
                if longitud > max_longitud:
                    max_fila, max_inicio, max_longitud = i, inicio, longitud
                inicio, longitud = -1, 0
        if longitud > max_longitud:
            max_fila, max_inicio, max_longitud = i, inicio, longitud
    return max_fila, max_inicio, max_longitud


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

    No retorna nada.
    """
    clear_screen()
    n = int(input("Numero de filas: "))
    m = int(input("Numero de butacas por fila: "))
    sala = [[0] * m for _ in range(n)]

    cargar_sala(sala)

    print("\nEstado inicial de las butacas:")
    mostrar_butacas(sala)

    fila = seleccionar_1_indice(n, "fila")
    butaca = seleccionar_1_indice(m, "butaca")
    if reservar(sala, fila, butaca):
        print("\nReserva exitosa.")
    else:
        print("\nLa butaca ya esta reservada.")

    print("\nEstado de las butacas despues de la reserva:")
    mostrar_butacas(sala)

    libres = butacas_libres(sala)
    print(f"\nCantidad de butacas libres: {libres}")

    fila, inicio, longitud = butacas_contiguas(sala)
    if fila != -1:
        print(f"\nLa secuencia mas larga de butacas libres contiguas esta en la fila {fila}")
        print(f"Desde la butaca {inicio} con una longitud de {longitud}.")
    else:
        print("\nNo hay secuencias de butacas libres contiguas.")
    return None


if __name__ == "__main__":
    main()
