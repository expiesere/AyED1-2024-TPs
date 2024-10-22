"""
Ejercicio 6

El método index permite buscar un elemento dentro de una lista, devolviendo la 
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se 
produce una excepción de tipo ValueError. Desarrollar un programa que cargue 
una lista con números enteros ingresados a través del teclado (terminando con -1) 
y permita que el usuario ingrese el valor de algunos elementos para visualizar la 
posición que ocupan, utilizando el método index. Si el número no pertenece a la 
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el 
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""

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
    Carga una lista con numeros enteros ingresados por el usuario, terminando con -1.

    Post:
        Devuelve una lista de numeros enteros ingresados por el usuario, excluyendo el -1 final.
    """
    lista = []
    while True:
        try:
            numero = int(input("Ingresa un numero entero (-1 para terminar): "))
            if numero == -1:
                break
            else:
                lista.append(numero)
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    return lista


def buscar_elemento(lista: List[int]) -> None:
    """
    Permite al usuario buscar elementos en la lista utilizando el metodo index.
    Aborta el proceso al tercer error detectado.

    Pre:
        lista de nUmeros enteros.

    Post:
        Imprime la posicion del elemento si se encuentra en la lista.
        Imprime un mensaje de error si el elemento no se encuentra en la lista.
        Aborta el proceso despues de tres errores.
    """
    errores = 0
    while errores < 3:
        try:
            elemento = int(input("Ingresa el numero que deseas buscar: "))
            posicion = lista.index(elemento)
            print(f"El numero {elemento} se encuentra en la posicion {posicion}.")
        except ValueError:
            errores += 1
            print(f"Error: El numero {elemento} no se encuentra en la lista. Intentos fallidos: {errores}")
            if errores == 3:
                print("...Deteniendo el programa.")
                break
    return None


if __name__ == "__main__":
    clear_screen()
    lista_numeros = cargar_lista()
    buscar_elemento(lista_numeros)
