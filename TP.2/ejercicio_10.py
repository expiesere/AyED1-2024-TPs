"""Ejercicio 10"""

import random as rn


def main():
    """Esta funcion crea dos listas:
    La primera lista de 10 elementos con numeros del 1 al 100
    La segunda lista con una funcion lambda filtramos todos los numeros impares
    """

    # Genera una lista de 10 elementos, los numeros se generan al azar del 1 al 100
    lista_azar = [rn.randint(1, 100) for i in range(10)]

    # Crea una lista nueva utilizando la lista anterior pero solo con
    # los elementos impares utilizando filter
    lista_impares = list(filter(lambda x: x % 2 != 0, lista_azar))

    # Imprime las dos listas por pantalla
    print(f"Lista original: {lista_azar}")
    print(f"Lista de impares: {lista_impares}")


if __name__ == "__main__":
    main()
