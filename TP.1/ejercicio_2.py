"""Ejercicio 2"""

def es_bisiesto(year):
    """
    Un año es bisiesto si es divisible por 4, pero no por 100, 
    a menos que también sea divisible por 400.

    Pre:
    - 'year' es un entero positivo.

    Post:
    - Devuelve 'True' si el año es bisiesto, de lo contrario, 'False'.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def valor_true_false(day, month, year):
    """
    Verifica si los componentes de la fecha son válidos.

     Pre:
     - 'day', 'month', 'year' son números enteros positivos.
     - 'month' está en un rango de 1 a 12.
     - 'day' está en un rango de 1 a 31.
     - 'year' es mayor que 0.

     Post:
     - Devuelve un diccionario con los valores de validez de día, mes y año.
    """
    dias_x_mes = DIAS_X_MES.copy()
    mes_valido = 1 <= month <= 12
    if mes_valido:
        if month == 2 and es_bisiesto(year):
            dias_x_mes[2] = 29
        dia_valido = 1 <= day <= dias_x_mes[month]
    else:
        dia_valido = False
    anio_valido = year > 0
    return {
        "dia_valido": dia_valido,
        "mes_valido": mes_valido,
        "año_valido": anio_valido,
    }


def mostrar_validacion(day, month, year):
    """
    Muestra el valor de la fecha invocando la funcion 'valor_true_false'.
    """
    validacion = valor_true_false(day, month, year)
    print(f"Valor de dia: {validacion['dia_valido']}")
    print(f"Valor de mes: {validacion['mes_valido']}")
    print(f"Valor de año: {validacion['año_valido']}")
    return None


def fecha_valida(day, month, year):
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
    dias_x_mes = DIAS_X_MES.copy()

    if year < 1 or month < 1 or month > 12 or day < 1:
        return False
    if month == 2 and es_bisiesto(year):
        dias_x_mes[2] = 29
    else:
        dias_x_mes[2] = 28
    if month in dias_x_mes:
        if day > dias_x_mes[month]:
            return False
    else:
        return False

    return True


def main():
    """
    Le solicita al usuario que ingrese una fecha y verifica 
    si es valida llamando a la funcion 'fecha_valida'.

    Pre:
    - El usuario ingresa tres valores positivos: dia, mes y año.

    Post:
    - Imprime si la fecha es valida o no.
    """
    try:
        day = int(input("\nIngrese el dia: "))
        month = int(input("Ingrese el mes: "))
        year = int(input("Ingrese el año: "))
    except ValueError:
        print("Dato no valido, ingrese valores numericos enteros positivos.")

    mostrar_validacion(day, month, year)

    if fecha_valida(day, month, year):
        print(f"La fecha {day}/{month}/{year} es valida.")
    else:
        print(f"La fecha {day}/{month}/{year} no es valida.")
    return None



DIAS_X_MES = {
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
