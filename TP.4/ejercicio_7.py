"""Ejercicio 7"""



def eliminar_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Elimina una subcadena de una cadena de caracteres utilizando rebanadas.

    Pre:
        -cadena (str): La cadena original.
        -posicion (int): La posicion inicial de la subcadena.
        -cantidad (int): La cantidad de caracteres de la subcadena.

    Post:
        -str: El resultado de La subcadena eliminada.
    """
    return cadena[:posicion] + cadena[posicion + cantidad :]


def eliminar_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Elimina una subcadena de una cadena de caracteres sin utilizar rebanadas.

    Pre:
        -cadena (str): La cadena original.
        -posicion (int): La posicion inicial de la subcadena.
        -cantidad (int): La cantidad de caracteres de la subcadena.

    Post:
        -str: El resultado de la subcadena eliminada.
    """
    resultado = ""
    for i in range(len(cadena)):
        if i < posicion or i >= posicion + cantidad:
            resultado += cadena[i]
    return resultado


def main() -> None:
    """
    Funcion principal que solicita al usuario una cadena, una posicion y una cantidad de caracteres.
    ELIMINA una subcadena y muestra el resultado con dos funciones: funcion con rebanadas y
    funcion sin rebanadas.
    :3
    """
    cadena = "Lic. en Gestion de Tecnologias de la Informacion"
    posicion = 25
    cantidad = 9

    print("Cadena original:", cadena)
    print("Posicion inicial:", posicion)
    print("Cantidad de caracteres:", cantidad)

    resultado_rebanadas = eliminar_subcadena_rebanadas(cadena, posicion, cantidad)
    print(f"\nCadena resultante (rebanadas): {resultado_rebanadas}")

    resultado_sin_rebanadas = eliminar_subcadena_sin_rebanadas(
        cadena, posicion, cantidad
    )
    print(f"Cadena resultante (sin rebanadas): {resultado_sin_rebanadas}")
    return None


if __name__ == "__main__":
    main()
