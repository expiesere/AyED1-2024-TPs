"""
Ejercicio 3

Desarrollar una función que devuelva una cadena de caracteres con el nombre del 
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán 
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función. 
Devolver una cadena vacía si el número de mes es inválido. La detección de meses 
inválidos deberá realizarse a través de excepciones.
"""

import os


def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.

    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


def nombre_del_mes() -> str:
    """
    Solicita al usuario que ingrese un numero de mes y devuelve el nombre del mes correspondiente.

    Post:
        El nombre del mes correspondiente o una cadena vacia si el numero es invalido.

    """
    meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]

    try:
        numero_mes = int(input("Ingresa el numero del mes (1-12): "))
        if 1 <= numero_mes <= 12:
            nombre_mes = meses[numero_mes - 1]
            print(f"El mes correspondiente es: {nombre_mes}")
            return nombre_mes
        else:
            raise ValueError("Numero de mes fuera de rango.")
    except ValueError as ve:
        print(f"Error: {ve}")
        return ""


if __name__ == "__main__":
    clear_screen()
    nombre_del_mes()
