def es_bisiesto(year):
    """
    Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.
    
    Pre:
    - 'year' es un entero positivo.

    Post:
    - Devuelve 'True' si el año es bisiesto, de lo contrario, 'False'.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def fecha_valida(day, month, year):
    """
    Verifica si la fecha ingresada es valida, utiliza el diccionario 'dia_x_mes = {mes:dia}' y la funcion 'es_bisiesto'.

    Pre:
    - 'day', 'month', 'year' son numeros enteros positivos.
    - 'month' esta en un rango de 1 a 12.
    - 'day' esta en un rango de 1 a 31.

    Post:
    - Devuelve 'True' si la fecha es valida, de lo contrario, 'False'.
    """
    if month < 1 or month > 12 or day < 1:
        return False


    if month == 2 and es_bisiesto(year):
        dias_x_mes[2] = 29
    else:
        dias_x_mes[2] = 28
    

    if month in dias_x_mes and day > dias_x_mes[month]:
        return False
    
    return True


def main():
    """
    Le solicita al usuario que ingrese una fecha y verifica si es valida llamando a la funcion 'fecha_valida'.

    Pre:
    - El usuario ingresa tres valores positivos: dia, mes y año.

    Post:
    - Imprime si la fecha es valida o no.
    """
    day = int(input("\nIngrese el dia: "))
    month = int(input("Ingrese el mes: "))
    year = int(input("Ingrese el año: "))

    if fecha_valida(day, month, year):
        print(f"La fecha {day}/{month}/{year} es valida.")
    else:
        print(f"La fecha {day}/{month}/{year} no es valida.")
    return None


dias_x_mes = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

if __name__ == "__main__":
    main()
