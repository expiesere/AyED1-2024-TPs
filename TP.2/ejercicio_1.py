"""Ejercicio 1"""

import random as rn


def cargar_lista():
    """
    Carga una lista con numeros al azar de cuatro digitos. La cantidad de elementos
    tambien es un numero al azar de dos digitos.
    """
    cantidad = rn.randint(1, 20)
    lista = [rn.randint(1, 10) for i in range(cantidad)]
    return lista


def producto_lista(lista):
    """
    Calcula y devuelve el producto de todos los elementos
    de la lista anterior.
    """
    producto = 1
    for numero in lista:
        producto *= numero
    return producto


def eliminar_valor(lista, valor):
    """
    Elimina todas las apariciones de un valor en la lista anterior.
    El valor a eliminar se ingresa desde el teclado y la función lo recibe como parametro.
    No utiliza listas auxiliares.
    """
    while valor in lista:
        lista.remove(valor)
    return lista


def es_capicua(lista):
    """
    Determina si el contenido de la lista es capicua,
    sin usar listas auxiliares.
    """
    return lista == lista[::-1]


def main():
    """Funcion principal del programa"""
    lista = cargar_lista()
    print("Lista cargada:", lista)

    producto = producto_lista(lista)
    print("Producto de todos los elementos:", producto)

    valor_a_eliminar = int(input("Ingrese el valor a eliminar: "))
    lista = eliminar_valor(lista, valor_a_eliminar)
    print("Resultado de eliminar el valor ingresado:", lista)

    print(f"¿La lista {lista} es capicua? ... {es_capicua(lista)}")
    return None


if __name__ == "__main__":
    main()
