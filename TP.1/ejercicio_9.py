"""Ejercicio 9"""

import random as rn
import os
from typing import Tuple

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def simular_peso_naranja() -> int:
    """
    Con la biblioteca random crea valores aleatorios que van a representar
    el peso de las naranjas.
    
    Post:
        -int: Peso de la naranja.
    """
    return rn.randint(150, 350)

def clasificar_naranjas(cantidad: int) -> Tuple:
    """
    Clasifica las naranjas en aptas para cajones y para jugo segun su peso.
    
    Pre:
        -cantidad, int: Cantidad de naranjas cosechadas.
    
    Post:
        -tuple: Numero de naranjas aptas para cajones, numero de naranjas para jugo.
    """
    aptas = 0
    para_jugo = 0
    for _ in range(cantidad):
        peso = simular_peso_naranja()
        if 200 <= peso <= 300:
            aptas += 1
        else:
            para_jugo += 1
    return aptas, para_jugo

def calcular_cajones_y_sobrantes(naranjas_aptas: int) -> Tuple:
    """
    Calcula el numero de cajones llenos y las naranjas sobrantes.
    
    Pre:
        - naranjas_aptas, int: Numero de naranjas aptas para cajones.
    
    Post:
        - tuple: Numero de cajones llenos, numero de naranjas sobrantes.
    """
    cajones_llenos = naranjas_aptas // 100
    sobrantes = naranjas_aptas % 100
    return cajones_llenos, sobrantes

def calcular_camiones_necesarios(cajones: int) -> int:
    """
    Calcula el numero de camiones necesarios para transportar los cajones.
    
    Pre:
        -cajones, int: Numero de cajones llenos.
    
    Post:
        -int: Numero de camiones necesarios.
    """
    capacidad_camion = 500  # kilogramos
    peso_cajon = 100 * 250 / 1000  # kilogramos (100 naranjas de 250 gramos promedio)
    cajones_por_camion = capacidad_camion // peso_cajon
    camiones_necesarios = cajones // cajones_por_camion
    if cajones % cajones_por_camion > 0:
        camiones_necesarios += 1
    return camiones_necesarios

def main() -> None:
    """
    Funcion principal que solicita la cantidad de naranjas cosechadas y muestra los resultados.

    No retorna nada.
    """
    clear_screen()
    cantidad_naranjas = int(input("Cantidad de naranjas cosechadas: "))
    naranjas_aptas, naranjas_para_jugo = clasificar_naranjas(cantidad_naranjas)
    cajones_llenos, sobrantes = calcular_cajones_y_sobrantes(naranjas_aptas)
    camiones_necesarios = calcular_camiones_necesarios(cajones_llenos)
    print(f"Naranjas aptas para cajones: {naranjas_aptas}")
    print(f"Naranjas para jugo: {naranjas_para_jugo}")
    print(f"Cajones llenos: {cajones_llenos}")
    print(f"Naranjas sobrantes: {sobrantes}")
    print(f"Camiones necesarios: {camiones_necesarios}")
    return None

if __name__ == "__main__":
    main()
