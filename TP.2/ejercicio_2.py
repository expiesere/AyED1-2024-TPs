"""Ejercicio 2"""

import random as rn


def generar_lista():
    """
    Genera una lista de N numeros aleatorios del 1 al 100.
    El valor de N lo ingresa el usuario.
    """
    n = int(input("Ingrese un numero entero positivo: "))
    lista = [rn.randint(1, 100) for i in range(n)]
    return lista


def tiene_repetidos(lista):
    """
    Recibe una lista como parametro y devuelve True si contiene algun elemento repetido.
    La función no modificar la lista.
    """
    return len(lista) != len(set(lista))  # Revisar SET, se puede usar!?


def elementos_unicos(lista):
    """
    Recibe una lista como parametro y devuelve una nueva lista con los elementos
    unicos de la lista original, sin importar el orden.
    """
    return list(set(lista))  # Revisar SET, se puede usar!?


def mostrar_menu():
    """Opciones"""
    print("1- Generar lista de numeros aleatorios")
    print("2- Verificar si la lista tiene elementos repetidos")
    print("3- Obtener elementos unicos de la lista")
    print("4- Salir")
    return None


def main():
    """Funcion principal del programa"""
    lista = []
    while True:
        mostrar_menu()
        opcion = input("\n...Seleccione una opcion: ")

        match opcion:

            case "1":
                lista = generar_lista()
                print("\nLista generada:", lista)
            case "2":
                if lista:
                    repetidos = tiene_repetidos(lista)
                    print("\n¿La lista tiene elementos repetidos?", repetidos)
                else:
                    print("\nPrimero debe generar una lista.")
            case "3":
                if lista:
                    lista_unicos = elementos_unicos(lista)
                    print("\nLista con elementos únicos:", lista_unicos)
                else:
                    print("\nPrimero debe generar una lista.")
            case "4":
                print("\nAdios!")
                break
            case _:
                print("\n...Opción no válida. Intente de nuevo.")
    return None


if __name__ == "__main__":
    main()
