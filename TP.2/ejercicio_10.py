"""Ejercicio 10"""

import random as rn
import os

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def main() -> None:
    """Esta funcion crea dos listas:
    La primera lista de 10 elementos con numeros del 1 al 100
    La segunda lista con una funcion lambda filtramos todos los numeros impares
    
    No retorna nada.
    """

    # Genera una lista de 10 elementos, los numeros se generan al azar del 1 al 100
    lista_azar = [rn.randint(1, 100) for i in range(10)]

    # Crea una lista nueva utilizando la lista anterior pero solo con
    # los elementos impares utilizando filter
    lista_impares = list(filter(lambda x: x % 2 != 0, lista_azar))

    # Imprime las dos listas por pantalla
    print(f"Lista original: {lista_azar}")
    print(f"Lista de impares: {lista_impares}")
    return None

if __name__ == "__main__":
    main()
