"""Ejercicio 6"""
import os

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


def extraer_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Extrae una subcadena de una cadena de caracteres utilizando rebanadas.

    Pre:
        -cadena (str): La cadena original.
        -posicion (int): La posicion inicial de la subcadena.
        -cantidad (int): La cantidad de caracteres de la subcadena.

    Post:
        -str: La subcadena extraida.
    """
    return cadena[posicion : posicion + cantidad]


def extraer_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Extrae una subcadena de una cadena de caracteres sin utilizar rebanadas.

    Pre:
        -cadena (str): La cadena original.
        -posicion (int): La posicion inicial de la subcadena.
        -cantidad (int): La cantidad de caracteres de la subcadena.

    Post:
        -str: La subcadena extraida.
    """
    subcadena = ""
    for i in range(posicion, posicion + cantidad):
        if i < len(cadena):
            subcadena += cadena[i]
    return subcadena


def main() -> None:
    """
    Funcion principal que ejecuta las demas funciones.

    No retorna nada.
    """
    clear_screen()
    cadena = "Lic. en Gestion de Tecnologias de la Informacion"
    posicion = 25
    cantidad = 9

    print("Cadena original:", cadena)
    print("Posicion inicial:", posicion)
    print("Cantidad de caracteres:", cantidad)

    subcadena_rebanadas = extraer_subcadena_rebanadas(cadena, posicion, cantidad)
    print(f"\nSubcadena extraida (rebanadas): {subcadena_rebanadas}")

    subcadena_sin_rebanadas = extraer_subcadena_sin_rebanadas(cadena, posicion, cantidad)
    print(f"Subcadena extraida (sin rebanadas): {subcadena_sin_rebanadas}")
    return None


if __name__ == "__main__":
    main()
