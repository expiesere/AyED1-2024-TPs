"""Ejercicio 4"""
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

def eliminar_valores(lista_original: List[int], lista_a_eliminar: List[int]) -> None:
    """
    Elimina los valores que se encuentren en ambas listas.

    Pre:
        -lista_original (List[int]): La lista original de numeros.
        -lista_a_eliminar (List[int]): La lista de numeros a eliminar de la lista original.
    """
    print(f"\nOriginal: {lista_original}")
    print(f"Lista de valores a eliminar: {lista_a_eliminar}")

    for valor in lista_a_eliminar:
        while valor in lista_original:
            lista_original.remove(valor)

    print(f"Resultado: {lista_original}")
    return None


def main() -> None:
    """
    Le solicita al usuario N cantidad de numeros para crear las listas.

    No retorna nada.
    """
    clear_screen()

    cantidad_numeros = int(input("Ingrese la cantidad de numeros a generar: "))
    lista_original = [rn.randint(1, 100) for i in range(cantidad_numeros)]
    cantidad_a_eliminar = int(input("Ingrese la cantidad de numeros a eliminar: "))
    lista_a_eliminar = [rn.randint(1, 100) for j in range(cantidad_a_eliminar)]
    eliminar_valores(lista_original, lista_a_eliminar)
    return None


if __name__ == "__main__":
    main()
