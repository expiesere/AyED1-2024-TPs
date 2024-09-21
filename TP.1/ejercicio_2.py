"""Ejercicio 2"""

def es_bisiesto(anio: int) -> bool:
    """
    Evalua si el es bisiesto.
    Para que un año sea bisiesto debe ser divisible por 4 pero no por 100,
    a menos que tambien sea divisible por 400.

    Pre:
    - 'anio' es un entero positivo.

    Post:
    - Devuelve 'True' si el año es bisiesto, de lo contrario, 'False'.
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def fecha_valida(day: int, month: int, year: int) -> bool:
    """
    Verifica si la fecha ingresada es valida, utiliza el
    diccionario 'dia_x_mes = {mes:dia}' y la funcion 'es_bisiesto'.

    Pre:
    - 'day', 'month', 'year' son numeros enteros positivos.
    - 'month' esta en un rango de 1 a 12.
    - 'day' esta en un rango de 1 a 31.
    - 'year' es mayor a 0.

    Post:
    - Devuelve 'True' si la fecha es valida, de lo contrario, 'False'.
    """
    copia = dias_x_mes.copy()

    if year < 1 or month < 1 or month > 12 or day < 1:
        return False
    if month == 2 and es_bisiesto(year):
        copia[2] = 29
    else:
        copia[2] = 28
    if month in copia:
        if day > copia[month]:
            return False
    else:
        return False

    return True


def main() -> None:
    """
    Le solicita al usuario que ingrese una fecha y verifica
    si es valida llamando a la funcion 'fecha_valida'.

    Pre:
    - El usuario ingresa tres valores positivos: dia, mes y año.

    Post:
    - Imprime si la fecha es valida o no.

    No retorna nada.
    """
    try:
        day = int(input("\nIngrese el dia: "))
        month = int(input("Ingrese el mes: "))
        year = int(input("Ingrese el año: "))
    except ValueError:
        print("Dato no valido, ingrese valores numericos enteros positivos.")

    if fecha_valida(day, month, year):
        print(f"La fecha {day}/{month}/{year} es valida.")
    else:
        print(f"La fecha {day}/{month}/{year} no es valida.")
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

#TYPE HINTSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
if __name__ == "__main__":
    main()
