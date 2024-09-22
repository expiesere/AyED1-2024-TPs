"""Ejercicio 10"""
import os
from typing import Tuple

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


def reemplazar_palabra(texto: str, palabra_vieja: str, palabra_nueva: str) -> Tuple[str, int]:
    """
    Reemplaza todas las apariciones de una palabra por otra en una cadena de caracteres.

    Pre:
        -texto (str): La cadena de caracteres original.
        -palabra_vieja (str): La palabra que se desea reemplazar.
        -palabra_nueva (str): La palabra nueva que reemplazara a la palabra vieja.

    Post:
        -tuple[str, int]: Una tupla que contiene la cadena de caracteres modificados y
                            el numero de reemplazos realizados.
    """
    palabras = texto.split()
    conteo = 0
    for i in range(len(palabras)):
        if palabras[i] == palabra_vieja:
            palabras[i] = palabra_nueva
            conteo += 1
    texto_nuevo = " ".join(palabras)
    return texto_nuevo, conteo


def main() -> None:
    """
    Funcion principal que ejecuta las demas funciones.

    No retorna nada.
    """
    clear_screen()
    texto = input("Introduzca una cadena de caracteres: ")
    total_reemplazos = 0

    while True:
        palabra_vieja = input("\nPalabra a reemplazar (-1 para terminar): ")
        if palabra_vieja == "-1":
            break
        palabra_nueva = input("Nueva palabra: ")

        texto, reemplazos = reemplazar_palabra(texto, palabra_vieja, palabra_nueva)
        total_reemplazos += reemplazos

        print(f"Texto modificado: {texto}")
        print(f"Numero total de reemplazos: {total_reemplazos}")

    print(f"Texto final: {texto}")
    print(f"Total de reemplazos realizados: {total_reemplazos}")
    return None

if __name__ == "__main__":
    main()
