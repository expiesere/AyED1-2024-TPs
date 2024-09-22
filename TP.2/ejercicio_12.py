"""Ejercicio 12"""
import os

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def registrar_ingresos():
    """
    Registra los numeros de socio que ingresan al club hasta que se ingrese un cero.

    Post:
        -list: Lista de numeros de socio que ingresaron al club.
    """
    ingresos = []
    while True:
        numero_socio = int(input("Numero de socio (0 para finalizar): "))
        if numero_socio == 0:
            break
        ingresos.append(numero_socio)
    return ingresos


def contar_ingresos(ingresos):
    """
    Cuenta cuantas veces ingreso cada socio al club.

    Pre:
        -ingresos (list): Lista de numeros de socio que ingresaron al club.

    Post:
        -dict: Diccionario con el numero de socio como clave y la cantidad de ingresos como valor.
    """
    conteo = {}

    for socio in ingresos:
        if socio in conteo:
            conteo[socio] += 1
        else:
            conteo[socio] = 1

    return conteo


def eliminar_socio(ingresos, numero_socio):
    """
    Elimina todos los ingresos de un socio dado de baja y muestra los registros antes y 
    despues de la eliminacion.

    Pre:
        -ingresos (list): Lista de numeros de socio que ingresaron al club.
        -numero_socio (int): Numero de socio que se dio de baja.

    Post:
        -tuple: Lista de ingresos antes de la eliminacion, lista de ingresos despues de 
        la eliminacion, cantidad de ingresos eliminados.
    """
    ingresos_antes = ingresos.copy()
    ingresos_despues = [socio for socio in ingresos if socio != numero_socio]
    eliminados = len(ingresos) - len(ingresos_despues)
    return ingresos_antes, ingresos_despues, eliminados


def main():
    """
    Funcion principal que coordina el registro, cuenta los ingresos y elimina un socio dado de baja.
    """
    clear_screen()
    ingresos = registrar_ingresos()
    conteo = contar_ingresos(ingresos)

    print("\nConteo de ingresos por socio:")
    for socio, cantidad in conteo.items():
        print(f"Socio {socio}: {cantidad} ingresos")

    numero_socio_baja = int(input("\nNumero de socio que se dio de baja: "))
    ingresos_antes, ingresos_despues, eliminados = eliminar_socio(ingresos, numero_socio_baja)

    print("\nRegistros de entrada antes de eliminar al socio:")
    print(ingresos_antes)
    print("\nRegistros de entrada después de eliminar al socio:")
    print(ingresos_despues)
    print(f"\nSe eliminaron {eliminados} ingresos del socio {numero_socio_baja}")
    return None


if __name__ == "__main__":
    main()
