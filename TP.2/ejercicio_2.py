"""Ejercicio 2"""

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

def generar_lista() -> List[int]:
    """
    Genera una lista de N numeros aleatorios del 1 al 100.
    El valor de N lo ingresa el usuario.

    Post:
        -List[int]: Lista con valores al azar con una longitud determinada por 
        el usuario.
    """
    n = int(input("Ingrese un numero entero positivo: "))
    try:
        lista = [rn.randint(1, 100) for i in range(n)]
    except ValueError:
        print("Error: Se debe ingresar un numero entero positivo.")
    return lista


def tiene_repetidos(lista: List[int]) -> bool:
    """
    Recibe una lista como parametro y devuelve True si contiene algun elemento repetido.

    Pre:
        -List[int]: Lista de numeros.

    Pre:
        -bool: True si hay elementos repetidos, de lo contrario False.
    """
    return len(lista) != len(set(lista))


def elementos_unicos(lista: List[int]) -> List[int]:
    """
    Recibe una lista como parametro y devuelve una nueva lista con los elementos
    unicos de la lista original, sin importar el orden.

    Pre: 
        -List[int]: Lista de numeros.

    Post:
        -List[int]: Lista con los elementos unicos.
    """
    return list(set(lista))


def mostrar_menu() -> None:
    """
    Opciones del menu principal.
    
    No retorna nada.
    """
    print("1- Generar lista de numeros aleatorios")
    print("2- Verificar si la lista tiene elementos repetidos")
    print("3- Obtener elementos unicos de la lista")
    print("4- Salir")
    return None


def main() -> None:
    """
    Funcion principal del programa donde se ejecutan cada una de las funciones.
    
    No retorna Nada.
    """
    lista = []
    clear_screen()
    while True:
        mostrar_menu()
        opcion = input("\n...Seleccione una opcion: ")

        match opcion:

            case "1":
                lista = generar_lista()
                print(f"\nLista generada: {lista}")
            case "2":
                if lista:
                    repetidos = tiene_repetidos(lista)
                    print(f"\n¿La lista tiene elementos repetidos? ... {repetidos}")
                else:
                    print("\nPrimero debe generar una lista.")
            case "3":
                if lista:
                    lista_unicos = elementos_unicos(lista)
                    print(f"\nLista con elementos únicos: {lista_unicos}")
                else:
                    print("\nPrimero debe generar una lista.")
            case "4":
                print("\n¡Adios!")
                break
            case _:
                print("\n...El valor ingresado no es valido, intente de nuevo.")
    return None


if __name__ == "__main__":
    main()
