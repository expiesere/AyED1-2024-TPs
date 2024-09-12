"""Ejercicio 7"""

import random as rn


def intercalar_listas(lista1, lista2):
    """
    Intercala los elementos de lista2 entre los elementos de lista1.
    Modifica lista1 en lugar de crear una nueva lista.

    Pre:
        -lista1 (list -> int)
        -lista2 (list -> int)
    """
    # Determina la longitud minima de las dos listas
    min_len = min(len(lista1), len(lista2))

    # Intercala los elementos de lista2 en lista1 utilizando .insert
    for i in range(min_len):
        lista1.insert(2 * i + 1, lista2[i])

    # Si lista2 es mas larga, agrega los elementos restantes al final de lista1
    if len(lista2) > min_len:
        lista1[len(lista1) :] = lista2[min_len:]
    return lista1


def main():
    """
    Genera listas aleatorias con la biblioteca random
    """
    longitud_lista1 = rn.randint(3, 10)
    longitud_lista2 = rn.randint(3, 10)
    lista1 = [rn.randint(0, 10) for i in range(longitud_lista1)]
    lista2 = [rn.randint(0, 10) for i in range(longitud_lista2)]

    # Muestra las listas generadas
    print(f"Lista 1 original: {lista1}")
    print(f"Lista 2 original: {lista2}")

    # Intercala los elementos de las listas
    intercalar_listas(lista1, lista2)

    # Muestra la lista intercalada
    print(f"Lista 1 intercalada: {lista1}")
    return None


if __name__ == "__main__":
    main()
