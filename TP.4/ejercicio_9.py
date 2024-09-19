"""Ejercicio 9"""


def limpiar_palabra(palabra: str) -> str:
    """
    Elimina los signos de puntuacion de una palabra.

    Pre:
        -palabra (str): La palabra de la cual se eliminaran los signos de puntuacion.

    Post:
        -str: La palabra sin signos de puntuacion.
    """
    return "".join(caracter for caracter in palabra if caracter.isalnum())


def ordenar_palabras_por_longitud(cadena: str) -> str:
    """
    Ordena las palabras de una cadena segun su longitud,
    manteniendo los signos de puntuacion en su lugar.

    Pre:
        -cadena (str): La cadena de entrada con palabras separadas por uno o mas espacios.

    Post:
        -str: Una nueva cadena con las palabras ordenadas por longitud,
        manteniendo los signos de puntuacion.
    """
    palabras = cadena.split()
    palabras_limpias = [limpiar_palabra(palabra) for palabra in palabras]
    palabras_ordenadas = sorted(palabras_limpias, key=len)
    resultado = []
    for palabra in palabras_ordenadas:
        for original in palabras:
            if limpiar_palabra(original) == palabra:
                resultado.append(original)
                palabras.remove(original)
                break
    return " ".join(resultado)


def main():
    """
    Funcion principal para ejecutar el programa.
    """
    cadena = "Lic. en Gestion de Tecnologias de la Informacion UADE"
    resultado = ordenar_palabras_por_longitud(cadena)
    print(resultado)
    return None


if __name__ == "__main__":
    main()
