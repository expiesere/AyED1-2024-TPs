"""Ejercicio 5"""
import os

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


def filtrar_palabras_ciclos(frase: str, n: int) -> str:
    """
    Filtra las palabras de una frase que tienen N o mas caracteres utilizando ciclos normales.

    Pre:
        -frase (str): La frase original.
        -n (int): El numero minimo de caracteres que deben tener las palabras.

    Post:
        -str: Una cadena con las palabras que tienen N o mas caracteres.
    """
    palabras = frase.split()
    resultado = []
    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)
    return " ".join(resultado)


def filtrar_palabras_comprension(frase: str, n: int) -> str:
    """
    Filtra las palabras de una frase que tienen N o
    mas caracteres utilizando listas por comprension.

    Pre:
        -frase (str): La frase original.
        -N (int): El numero minimo de caracteres que deben tener las palabras.

    Post:
        -str: Una cadena con las palabras que tienen N o mas caracteres.
    """
    return " ".join([palabra for palabra in frase.split() if len(palabra) >= n])


def filtrar_palabras_filter(frase: str, n: int) -> str:
    """
    Filtra las palabras de una frase que tienen N o mas caracteres utilizando la funcion filter.

    Pre:
        -frase (str): La frase original.
        -N (int): El numero minimo de caracteres que deben tener las palabras.

    Post:
        -str: Una cadena con las palabras que tienen N o mas caracteres.
    """
    return " ".join(filter(lambda palabra: len(palabra) >= n, frase.split()))


def main() -> None:
    """
    Funcion principal que ejecuta las demas funciones.

    No retorna nada.
    """
    clear_screen()
    frase = input("Escriba una frase: ")
    n = int(input("¿Cual es el numero minimo de caracteres?: "))

    print(f"\nUsando ciclos normales apartir de {n} o mas caracteres:")
    print(filtrar_palabras_ciclos(frase, n))

    print(f"\nUsando listas por comprension apartir de {n} o mas caracteres:")
    print(filtrar_palabras_comprension(frase, n))

    print(f"\nUsando la funcion filter apartir de {n} o mas caracteres:")
    print(filtrar_palabras_filter(frase, n))
    return None


if __name__ == "__main__":
    main()
