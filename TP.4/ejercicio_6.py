"""Ejercicio 6"""


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
    Funcion principal que solicita al usuario una cadena, una posicion y una cantidad de caracteres.
    Muestra una subcadena EXTRAIDA con dos funciones: funcion con rebanadas y
    funcion sin rebanadas.
    :3
    """
    cadena = "Lic. en Gestion de Tecnologias de la Informacion"
    posicion = 25
    cantidad = 9

    print("Cadena original:", cadena)
    print("Posicion inicial:", posicion)
    print("Cantidad de caracteres:", cantidad)

    subcadena_rebanadas = extraer_subcadena_rebanadas(cadena, posicion, cantidad)
    print(f"\nSubcadena extraida (rebanadas): {subcadena_rebanadas}")

    subcadena_sin_rebanadas = extraer_subcadena_sin_rebanadas(
        cadena, posicion, cantidad
    )
    print(f"Subcadena extraida (sin rebanadas): {subcadena_sin_rebanadas}")
    return None


if __name__ == "__main__":
    main()
