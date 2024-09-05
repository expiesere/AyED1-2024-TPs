"""Ejercicio 4"""


def calcular_vuelto(total_compra, dinero_recibido):
    """
    Calcula el vuelto x billete que debe entregarse al cliente con una lista
    que contiene los siguientes valores: '2000, 1000, 500, 200, 100, 50, 10'

    Pre:
        -Total de la compra (gasto)
        -Tatal del dinero recibido del cliente (pago)
    Post:
        -Diccionario con la cantidad de billetes a devolver para compensar el vuelto
    """
    if dinero_recibido < total_compra:
        return "...El dinero recibido es insuficiente."

    vuelto = dinero_recibido - total_compra
    resultado = {}

    for billete in billetes:
        cantidad_billetes = vuelto // billete
        if cantidad_billetes > 0:
            resultado[billete] = cantidad_billetes
            vuelto -= cantidad_billetes * billete

    if vuelto != 0:
        return "...No se pudo entregar el cambio exacto."
    return resultado


def main():
    """
    Solicita al usuario el total de la compra y el dinero recibido,
    y muestra el vuelto a entregar.
    """
    try:
        total_compra = int(input("Ingrese el total de la compra: "))
        dinero_recibido = int(input("Ingrese el dinero recibido: "))
    except ValueError:
        print("Error: Ingrese valores numericos enteros.")
        return

    resultado = calcular_vuelto(total_compra, dinero_recibido)

    if isinstance(resultado, str):
        print(resultado)
    else:
        print("El vuelto a entregar es:")
        for billete, cantidad in resultado.items():
            print(f"{cantidad} billete(s) de ${billete}")


billetes = [2000, 1000, 500, 200, 100, 50, 10]

if __name__ == "__main__":
    main()
