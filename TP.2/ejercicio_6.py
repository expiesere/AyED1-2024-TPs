"""Ejercicio 6"""
import os
from typing import  List

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def normalizar(lista: List[int]) -> List[float]:
    """
    Normaliza una lista de numeros enteros para 
    que la suma de todos sus elementos sea 1.0

    Pre:
        -lista de numeros enteros (int)

    Post:
        -lista de numeros normalizados (float)
    """
    suma = sum(lista)
    return [x / suma for x in lista]


# Funcion principal
def main() -> None:
    """
    Solicita al usuario que ingrese una lista numeros enteros separados por comas,
    normaliza la lista y muesta el resultado.

    No retorna nada.
    """
    clear_screen()
    while True:
        try:
            # Solicita al usuario que ingrese los valores de la lista
            datos = input("\nIngresa una secuencia de numeros separados solo por comas: ")
            lista = list(map(int, datos.split(",")))
            break  # Sale del bucle si la conversion es exitosa
        except ValueError:
            print("Error: Se deben ingresar solo numeros enteros separados por comas.")

    lista_normalizada = normalizar(lista)
    print(f"Lista original: {lista}")
    print(f"Lista normalizada: {lista_normalizada}")
    print(f"Suma de elementos normalizados: {sum(lista_normalizada)}")
    return None


if __name__ == "__main__":
    main()
