"""Ejercicio 9"""
import os

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def main() -> None:
    """Le solicita al usuario dos valores: A y B
    Estos valores van a ser el rango para generar una lista por
    comprension de los multiplos de 7 que no son multiplo de 5.

    -x for x in: Esta es la lista por compresion
    -range(A, B + 1): Secuencia de numeros de A a B inclusive
    -if x % 7 == 0 AND x % 5 != 0: Filtra todos los multilplos de 7 que no son multilplo de 5
    
    No retorna nada.
    """
    clear_screen()

    # Solicita al usuario que ingrese los valores de A y B
    a = int(input("Ingresa el valor de A: "))
    b = int(input("Ingresa el valor de B: "))

    # Generar la lista por comprension
    multiplos = [x for x in range(a, b + 1) if x % 7 == 0 and x % 5 != 0]

    # Imprimir la lista generada
    print(f"Los multiplos de 7 que no son multiplos de 5 entre {a} y {b} son: {multiplos}")
    return None


if __name__ == "__main__":
    main()
