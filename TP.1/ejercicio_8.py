"""Ejercicio 8"""
import os
from tabulate import tabulate

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def dia_de_la_semana(day: int, month: int, year: int) -> int:
    """
    Calcula el dia de la semana para una fecha dada.
    
    Pre:
        -day (int): Dia del mes.
        -month (int): Mes del año.
        -year (int): Año.

    Post:
        -int: Dia de la semana (0 para domingo, 1 para lunes, ..., 6 para sabado).
    """
    if month < 3:
        month = month + 10
        year = year - 1
    else:
        month = month - 2
    siglo = year // 100
    year2 = year % 100
    dia_semana = ((20 * month - 2) + day + year2 + (year2 // 4) - (2 * siglo)) % 7

    if dia_semana < 0:
        dia_semana = dia_semana + 7
    return dia_semana

def imprimir_calendario(month: int, year: int) -> None:
    """
    Imprime el calendario de un mes y año especificos.

    Pre:
        -month (int): Mes del año (1-12).
        -year (int): Año.
    """
    # Dias de cada mes
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Verificar si es año bisiesto
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        dias_mes[1] = 29

    # Obtener el dia de la semana del primer dia del mes
    primer_dia = dia_de_la_semana(1, month, year)

    # Crear la estructura del calendario
    calendario = [["" for _ in range(7)] for _ in range(6)]
    dia = 1
    for semana in range(6):
        for dia_semana in range(7):
            if semana == 0 and dia_semana < primer_dia:
                continue
            if dia > dias_mes[month - 1]:
                break
            calendario[semana][dia_semana] = dia
            dia += 1

    # Imprimir el calendario usando tabulate
    print(tabulate(
            calendario,
            headers=["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"],
            tablefmt="grid",))
    return None

def main() -> None:
    """
    Funcion principal que solicita al usuario el mes y el año, 
    y luego imprime el calendario correspondiente.

    No retorna nada.
    """
    clear_screen()
    # Solicitar entrada del usuario
    month = int(input("Introduce el mes (1-12): "))
    year = int(input("Introduce el año: "))

    # Imprimir el calendario para el mes y año ingresados
    imprimir_calendario(month, year)
    return None

if __name__ == "__main__":
    main()
