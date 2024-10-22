"""
Ejercicio 1

Desarrollar una función para ingresar a través del teclado un número natural. La 
función rechazará cualquier ingreso inválido de datos utilizando excepciones y 
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese 
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón 
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea 
correcto. Escribir también un programa que permita probar el correcto funciona
miento de la misma.
"""

import os


def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.

    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


def evaluar_input() -> int:
    """
    Solicita al usuario que ingrese un numero natural a traves del teclado.

    La funcion valida que la entrada sea un numero entero mayor que 0.
    Si la entrada no es valida, se muestra un mensaje de error especifico.

    Returns:
        int: El numero natural ingresado por el usuario.
    Raise:
        ValueError: Si el numero ingresado no es mayor que 0.
    Except:
        ValueError: Si el numero ingresado no es un entero.
    """
    while True:
        try:
            numero = int(input("...Ingresa un numero natural: "))
            if numero <= 0:
                raise ValueError("El numero debe ser mayor que 0.")
            print(f"Has ingresado el numero: {numero}")
            continue
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    return None


if __name__ == "__main__":
    clear_screen()
    evaluar_input()
