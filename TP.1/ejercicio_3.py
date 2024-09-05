"""Ejercicio 3"""


def calcular_gasto(viajes, tarifa_maxima):
    """
    Calcula el gasto total en viajes segun la cantidad de viajes realizados y
    la tarifa maxima.

    Pre:
        -Cantidad de viajes realizados en un mes
        -Tarifa maxima del pasaje

    Post:
        -Gasto total de viajes
    """
    if viajes <= 20:
        return viajes * tarifa_maxima
    elif 21 <= viajes <= 30:
        return viajes * tarifa_maxima * 0.8
    elif 31 <= viajes <= 40:
        return viajes * tarifa_maxima * 0.7
    else:
        return viajes * tarifa_maxima * 0.6


def solicitar_cantidad_viajes():
    """
    Le solicita al usuario que ingrese la cantidad de viajes realizados en un mes.
    """
    while True:
        try:
            viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
            if viajes < 0:
                print("Por favor, ingrese un número positivo.")
            else:
                return viajes
        except ValueError:
            print("Dato no válido, por favor ingrese un número entero.")


def main():
    """
    Invoca la funcion 'solicitar_cantidad_viajes' para que el usuario ingrese
    cantidad de viajes x mes y 'calcular_gasto' para evaluar el gasto total.
    """
    for tarifa in tarifas_maximas:
        viajes = solicitar_cantidad_viajes()
        gasto = calcular_gasto(viajes, tarifa)
        print(
            f"Con {viajes} viajes y una tarifa máxima de {tarifa}, el gasto total es: {gasto}"
        )
    return None


tarifas_maximas = [100, 150, 200]


if __name__ == "__main__":
    main()
