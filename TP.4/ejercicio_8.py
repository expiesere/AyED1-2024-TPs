"""Ejercicio 8"""



def ultimos_n_caracteres(cadena: str, n: int) -> str:
    """
    Devuelve una subcadena con los últimos N caracteres de una cadena dada.

    Pre:
        -cadena (str): La cadena original.
        -n (int): El numero de caracteres a extraer desde el final de la cadena.

    Post:
        -str: Subcadena con los ultimos N caracteres.
    """
    longitud = len(cadena)
    subcadena = ""
    for i in range(longitud - n, longitud):
        if i >= 0:
            subcadena += cadena[i]
    return subcadena


def main() -> None:
    """
    Funcion principal para verificar el comportamiento de
    ultimos_n_caracteres_sin_rebanadas.
    """
    cadena = "Lic. en Gestion de Tecnologias de la Informacion"
    n = 9
    resultado = ultimos_n_caracteres(cadena, n)
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
