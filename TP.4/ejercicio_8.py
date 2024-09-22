"""Ejercicio 8"""
import os

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


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
    Funcion principal que ejecuta las demas funciones.

    No retornada nada
    """
    clear_screen()
    cadena = "Lic. en Gestion de Tecnologias de la Informacion"
    n = 9
    resultado = ultimos_n_caracteres(cadena, n)
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
