"""Ejercicio 7"""
import os
from typing import Tuple


def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def es_bisiesto(anio: int) -> bool:
    """
    Un año es bisiesto si es divisible por 4, pero no por 100,
    a menos que también sea divisible por 400.

    Pre:
    - 'year' es un entero positivo.

    Post:
    - Devuelve 'True' si el año es bisiesto, de lo contrario, 'False'.
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si la fecha ingresada es valida, utiliza el
    diccionario 'dia_x_mes = {mes:dia}' y la funcion 'es_bisiesto'.

    Pre:
    - 'dia', 'mes', 'anio' son numeros enteros positivos.
    - 'mes' esta en un rango de 1 a 12.
    - 'dia' esta en un rango de 1 a 31.
    - 'anio' es mayor a 0.

    Post:
    - Devuelve 'True' si la fecha es valida, de lo contrario, 'False' y explota.
    """
    copia = dias_x_mes.copy()

    if anio < 1 or mes < 1 or mes > 12 or dia < 1:
        return False
    if mes == 2 and es_bisiesto(anio):
        copia[2] = 29
    else:
        copia[2] = 28
    if mes in dias_x_mes:
        if dia > copia[mes]:
            return False
    else:
        return False

    return True


def dia_siguiente(dia: int, mes: int, anio: int) -> Tuple[int, int, int]:
    """
    Calcula el dia siguiente a la fecha dada.

    Pre:
    - dia: int, mes: int, anio: int, son numeros enteros positivos.
    - La fecha ingresada es válida.

    Post:
    - Tuple: Devuelve tres enteros correspondientes al dia siguiente.
    """
    clear_screen()
    copia = dias_x_mes.copy()

    if es_bisiesto(anio):
        copia[2] = 29

    dia += 1

    if dia > copia[mes]:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
    return dia, mes, anio


def sumar_dias(dia: int, mes: int, anio: int, n: int) -> Tuple[int, int, int]:
    """
    Suma N cantidad de dias a la fecha dada.

    Pre:
    - dia: int, mes: int, año: int: Enteros positivo.
    - n: int: Entero positivo.

    Post:
    - tuple: Devuelve tres enteros correspondientes a la nueva fecha.
    """
    for _ in range(n):
        dia, mes, anio = dia_siguiente(dia, mes, anio)
    return dia, mes, anio


def dias_entre_fechas(dia1: int, mes1: int, anio1: int, dia2: int, mes2: int, anio2: int) -> int:
    """
    Calcula la cantidad de dias entre dos fechas.

    Pre:
    - 'dia1', 'mes1', 'anio1', 'dia2', 'mes2', 'anio2' son numeros enteros positivos.
    - Las fechas ingresadas son validas.

    Post:
    - Devuelve un entero correspondiente a la cantidad de dias entre las dos fechas.
    """
    dias_totales1 = (
        dia1
        + sum(dias_x_mes[m] for m in range(1, mes1))
        + (anio1 * 365)
        + (anio1 // 4 - anio1 // 100 + anio1 // 400)
    )
    dias_totales2 = (
        dia2
        + sum(dias_x_mes[m] for m in range(1, mes2))
        + (anio2 * 365)
        + (anio2 // 4 - anio2 // 100 + anio2 // 400)
    )
    return dias_totales2 - dias_totales1


def main() -> None:
    """
    Le solicita al usuario que ingrese una fecha y realiza operaciones segun la opcion seleccionada.

    No retorna nada.
    """
    clear_screen()
    while True:
        print("\nSeleccione una opcion:")
        print("1. Sumar N dias a una fecha")
        print("2. Calcular la cantidad de dias entre dos fechas")
        print("3. Salir")
        opcion = input("...Seleccione una opcion: ")

        match opcion:
            case "1":
                try:
                    day = int(input("\nIngrese el dia: "))
                    month = int(input("Ingrese el mes: "))
                    year = int(input("Ingrese el año: "))
                    num = int(input("Ingrese el numero de dias a sumar: "))
                except ValueError:
                    print("Dato no valido, ingrese valores numericos enteros positivos.")
                    continue

                if fecha_valida(day, month, year):
                    nuevo_dia, nuevo_mes, nuevo_año = sumar_dias(day, month, year, num)
                    print(f"Fecha original: {day}/{month}/{year}")
                    print(f"Fecha después de sumar {num} días: {nuevo_dia}/{nuevo_mes}/{nuevo_año}")
                else:
                    print("Fecha no válida.")

            case "2":
                try:
                    dia1 = int(input("\nIngrese el primer dia: "))
                    mes1 = int(input("Ingrese el primer mes: "))
                    año1 = int(input("Ingrese el primer año: "))
                    dia2 = int(input("\nIngrese el segundo dia: "))
                    mes2 = int(input("Ingrese el segundo mes: "))
                    año2 = int(input("Ingrese el segundo año: "))
                except ValueError:
                    print("Dato no valido, ingrese valores numericos enteros positivos.")
                    continue

                if fecha_valida(dia1, mes1, año1) and fecha_valida(dia2, mes2, año2):
                    dias = dias_entre_fechas(dia1, mes1, año1, dia2, mes2, año2)
                    print(f"Dias entre {dia1}/{mes1}/{año1} y {dia2}/{mes2}/{año2}: {dias} dias")
                else:
                    print("Una o ambas fechas no son validas.")

            case "3":
                print("\nAdios!")
                break

            case _:
                print("Opcion no válida, intente de nuevo.")
    return None


dias_x_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

if __name__ == "__main__":
    main()
