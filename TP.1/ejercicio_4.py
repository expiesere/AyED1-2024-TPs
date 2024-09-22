"""Ejercicio 4"""
import os
from typing import Dict


def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def calcular_vuelto(total_compra: int, dinero_recibido: int) -> Dict:
    """
    Calcula el vuelto por billete que debe entregarse con una lista
    que contiene los siguientes valores: '2000, 1000, 500, 200, 100, 50, 10'

    Pre:
        - total_compra (int): El total de la compra.
        - dinero_recibido (int): El dinero recibido del cliente.

    Post:
        - dict: Diccionario con la cantidad de billetes a devolver para compensar el vuelto,
              o un mensaje de error.
    """
    if dinero_recibido < total_compra:
        return {"error": "Dinero insuficiente."}
    elif dinero_recibido == total_compra:
        return {"mensaje": "Pago realizado con exito."}

    vuelto = dinero_recibido - total_compra
    resultado = {}

    for billete in billetes:
        cantidad_billetes = vuelto // billete
        if cantidad_billetes > 0:
            resultado[billete] = cantidad_billetes
            vuelto -= cantidad_billetes * billete

    if vuelto != 0:
        return {"error": "No se pudo entregar el cambio exacto."}

    return resultado


def main() -> None:
    """
    Solicita al usuario el total de la compra y el dinero recibido para pagar, y
    muestra el vuelto a entregar invocando la funcion 'calcular_vuelto'.

    No retorna nada.
    """
    clear_screen()
    while True:
        try:
            total_compra = int(input("Total de su compra:"))
            dinero_recibido = int(input("Ingrese con cuanto paga:"))
            if total_compra <= 0 or dinero_recibido <= 0:
                raise ValueError("Error: Los valores deben ser numeros mayores a 0.")
            break
        except ValueError:
            print("Error: Los valores deben ser numeros mayores a 0.")

    resultado = calcular_vuelto(total_compra, dinero_recibido)

    if "error" in resultado:
        print(resultado["error"])
    elif "mensaje" in resultado:
        print(resultado["mensaje"])
    else:
        print("Vuelto a entregar es:")
        for billete, cantidad in resultado.items():
            print(f"{cantidad} billete(s) de ${billete}")
    return None

billetes = [2000, 1000, 500, 200, 100, 50, 10, 5]

if __name__ == "__main__":
    main()
