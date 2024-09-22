"""Ejercicio 3"""
import os

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def obtener_valor_pasaje(cantidad_viajes: int) -> float:
    """
    Devuelve el valor del pasaje segun la cantidad de viajes realizados.

    Pre:
    - cantidad_viajes es un entero positivo.

    Post:
    - Devuelve el valor del pasaje con el descuento correspondiente.
    """
    tarifa_maxima = 100.0  # hipotetico caso de que la tarifa vale $ 100 °0°/

    if cantidad_viajes <= 20:
        valor_pasaje = cantidad_viajes * tarifa_maxima
    elif 21 <= cantidad_viajes <= 30:
        valor_pasaje = cantidad_viajes * (tarifa_maxima * 0.80)  # 20% de descuento
    elif 31 <= cantidad_viajes <= 40:
        valor_pasaje = cantidad_viajes * (tarifa_maxima * 0.70)  # 30% de descuento
    else:
        valor_pasaje = cantidad_viajes * (tarifa_maxima * 0.60)  # 40% de descuento
    return valor_pasaje


def main() -> None:
    """
    Solicita al usuario la cantidad de viajes realizados y muestra el valor del pasaje.

    Pre:
    - El usuario ingresa un numero entero positivo.

    Post:
    - Muestra el valor del pasaje con el descuento.

    No retorna nada.
    """
    clear_screen()
    while True:
        try:
            cantidad_viajes = int(input("Cantidad de viajes realizados: "))
            if cantidad_viajes >= 1:
                valor_pasaje = obtener_valor_pasaje(cantidad_viajes)
                print(f"El valor del pasaje es: ${valor_pasaje:.2f}")
            else:
                print("Debe ser un numero positivo.")
        except ValueError:
            print("Error: Ingrese solo numeros enteros positivos.")
            continue
    return None


if __name__ == "__main__":
    main()
