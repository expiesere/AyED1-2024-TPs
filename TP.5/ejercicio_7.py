"""
Ejercicio 7

Escribir un programa que juegue con el usuario a adivinar un número. El programa 
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para 
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que 
tiene que adivinar es mayor o menor que el ingresado. Cuando consiga 
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar 
el número. Si el usuario introduce algo que no sea un número se mostrará un 
mensaje en pantalla y se lo contará como un intento más.
"""

import random as rn
import os


def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.

    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


def juego_adivinar_num() -> None:
    """
    Genera un numero al azar entre 1 y 500, el usuario debe adivinar el numero ingresando un entero.
    Informa si el numero a adivinar es mayor o menor que el ingresado.
    Cuenta e imprime la cantidad de intentos que se realizaron para adivinar el numero.
    Maneja entradas no validas contandols como un intento mas.
    """
    num_random = rn.randint(1, 500)
    #print(num_random)
    intentos = 0

    while True:
        try:
            num_ingresado = int(input("\nAdivina cual es el numero que esta entre 1 y 500 (-1 para rendirse): "))
            intentos += 1
            if num_ingresado == -1:
                print(f"\n¡Perdiste! El numero era {num_random}")
                break
            elif num_ingresado < num_random:
                print(f"...Pista: El numero a adivinar es mayor a {num_ingresado}.")
            elif num_ingresado > num_random:
                print(f"...Pista: El numero a adivinar es menor a {num_ingresado}.")
            else:
                print(f"\n¡Felicidades! Adivinaste el numero {num_random} en {intentos} intentos.")
                break
        except ValueError:
            intentos += 1
            print("Error: Debes ingresar un numero entero valido.")
    return None


if __name__ == "__main__":
    clear_screen()
    juego_adivinar_num()
