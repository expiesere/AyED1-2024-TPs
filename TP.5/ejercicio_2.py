"""
Ejercicio 2

Realizar una función que reciba como parámetros dos cadenas de caracteres con
teniendo números reales, sume ambos valores y devuelva el resultado como un 
número real. Devolver -1 si alguna de las cadenas no contiene un número válido, 
utilizando manejo de excepciones para detectar el error.
"""

import os


def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.

    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


def sum_(cadena1: str, cadena2: str) -> int:
    """
    Suma dos numeros que son ingresados por el usuario como cadenas de caracteres.

    Pre:
        La primera cadena que contiene un numero real.
        La segunda cadena que contiene un numero real.

    Post:
        La suma de los dos numeros.
        -1 si alguna cadena no es valida.
    """
    try:
        numero1 = int(cadena1)
        numero2 = int(cadena2)
        resultado = numero1 + numero2
        print(f"...Resultado: {resultado}")
        return
    except ValueError:
        print(f"Error: -1")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return None


if __name__ == "__main__":
    clear_screen()
    cadena1 = input("Ingresa el primer numero: ")
    cadena2 = input("Ingresa el segundo numero: ")
    sum_(cadena1, cadena2)
