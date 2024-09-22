"""Ejercicio 1"""
import os

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


def es_capicua(cadena: str) -> bool:
    """
    Determina si una cadena de caracteres es palindromo (capicua), una cadena es capicua si
    se lee igual de izquierda a derecha que de derecha a izquierda.

    Pre:
        -cadena (str): Cadena de caracteres a evaluar.

    Post:
        -bool: True si la cadena es capicua, False en caso contrario.

    """
    longitud = len(cadena)
    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - 1 - i]:
            return False
    return True


def main() -> None:
    """
    Funcion principal que ejecuta las demas funciones.

    No retorna nada.
    """
    clear_screen()
    cadena = input("Escriba una cadena de caracteres para determinar si es capicua: ")
    if es_capicua(cadena):
        print(f'"{cadena}" es una cadena capicua.')
    else:
        print(f'"{cadena}" no es una cadena capicua.')
    return None


if __name__ == "__main__":
    main()
