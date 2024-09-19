"""Ejercicio 2"""



def centrar_cadena(cadena: str) -> None:
    """
    Lee una cadena de caracteres e imprime la cadena centrada en una pantalla
    de 80 columnas.

    Pre:
        -cadena (str): La cadena de caracteres a centrar e imprimir.
    """
    columnas = 80
    espacios = (columnas - len(cadena)) // 2
    cadena_centrada = " " * espacios + cadena
    print(cadena_centrada)
    return None


def main() -> None:
    """
    Funcion principal que solicita al usuario una cadena de caracteres y
    la imprime centrada.
    """
    cadena = input("Escriba una cadena de caracteres: ")
    centrar_cadena(cadena)
    return None


if __name__ == "__main__":
    main()
