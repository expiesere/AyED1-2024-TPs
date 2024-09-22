"""Ejercicio 5"""

import random as rn
import os
from typing import  List

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def esta_ordenada(lista: List[int]) -> bool:
    """
    Verifica si la lista esta ordenada en forma ascendente.
    
    Pre:
        -lista (List[int]): Lista de numeros enteros a verificar.
    
    Post:
        -bool: True si la lista esta ordenada en forma ascendente, de lo contrario, False.
    """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def main() -> None:
    """
    Programa para verificar el comportamiento de la funcion 'esta_ordenada' con listas
    generadas al azar.

    No retorna nada.
    """

    clear_screen()
    # Solicita al usuario la cantidad de numeros a generar
    cantidad_numeros = int(input("Ingrese la cantidad de numeros a generar: "))

    # Generar la lista con numeros aleatorios
    lista = [rn.randint(1, 100) for i in range(cantidad_numeros)]

    # Mostrar la lista generada
    print(f"Lista generada: {lista}")

    # Verificar si la lista esta ordenada
    resultado = esta_ordenada(lista)
    print(f"¿La lista esta ordenada? ... {resultado}")
    return None


if __name__ == "__main__":
    main()
