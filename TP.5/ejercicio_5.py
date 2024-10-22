"""
Ejercicio 5

La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del 
módulo math. Escribir un programa que utilice esta función para calcular la raíz 
cuadrada de un número cualquiera ingresado a través del teclado. El programa 
debe utilizar manejo de excepciones para evitar errores si se ingresa un número 
negativo.
"""

import math
import os


def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.

    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


def raiz_cuadrada() -> None:
    """
    Solicita al usuario un numero y calcula su raiz cuadrada.
    Maneja excepciones para numeros negativos.
    """
    try:
        numero = int(input("Ingresa un numero: "))
        if numero < 0:
            raise ValueError("No se puede calcular la raiz cuadrada de un numero negativo.")
        raiz_cuadrada = math.sqrt(numero)
        print(f"La raiz cuadrada de {numero} es {raiz_cuadrada}")
    except ValueError as e:
        print(f"Error: {e}")
    return None


if __name__ == "__main__":
    clear_screen()
    raiz_cuadrada()
