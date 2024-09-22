"""Ejercicio 1"""

import random as rn
import os
from typing import List

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def cargar_lista() -> List[int]:
    """
    Carga una lista con numeros al azar de cuatro digitos. La cantidad de elementos
    tambien es un numero al azar de dos digitos.

    Post:
        -List[int]: Retorna una lista con una longitud al azar y elementos enteros al azar.
    """
    cantidad = rn.randint(1, 20)
    lista = [rn.randint(1, 10) for i in range(cantidad)]
    return lista


def producto_lista(lista: List[int]) -> int:
    """
    Calcula y devuelve el producto de todos los elementos
    de la lista.

    pda: Producto de los elementos de la lista o la sumatoria como en el ejemplo resuelto?

    Pre:
        -List[int]: Lista de numeros enteros.

    Post: 
        -int: Producto de todos los elementos en la lista.
    """
    producto = 1
    for numero in lista:
        producto *= numero
    return producto


def eliminar_valor(lista: List[int], valor: int) -> List[int]:
    """
    Elimina todas las apariciones de un valor en la lista anterior, el valor se ingresa por teclado.

    Pre:
        -valor(int): Valor a eliminar ingresado por el usuario.
        -List[int]: Lista a la que se le va eliminar el valor.

    Post:
        -List[int]: Lista con el valor eliminado.
    """
    while valor in lista:
        lista.remove(valor)
    return lista


def es_capicua(lista: List[int]) -> bool:
    """
    Determina si el contenido de la lista es capicua, una lista es capicua
    si se lee de la misma manera de ambos lados.

    Pre:
        -List[int]: Lista para evaluar si su contenido es capicua.

    Post:
        -bool: True si la lista es capicua, de lo contrario, False.
    """
    return lista == lista[::-1]


def main() -> None:
    """
    Funcion principal del programa que ejecuta cada una de las funciones

    No retorna nada.
    """
    clear_screen()
    lista = cargar_lista()
    print("Lista cargada:", lista)

    producto = producto_lista(lista)
    print(f"Producto de todos los elementos: {producto}")

    valor_a_eliminar = int(input("Ingrese el valor a eliminar: "))
    print(f"Resultado de eliminar el valor ingresado: {eliminar_valor(lista, valor_a_eliminar)}")

    print(f"¿La lista {lista} es capicua? ... {es_capicua(lista)}")
    return None


if __name__ == "__main__":
    main()
