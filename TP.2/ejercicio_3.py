"""Ejercicio 3"""
import os

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

clear_screen()
# Solicita al usuario que ingrese el valor de n
n = int(input("Ingresa un numero entero: "))

# Crear una lista con los cuadrados de los numeros entre 1 y N
cuadrados = [i**2 for i in range(1, n + 1)]

# Imprime los ultimos 10 valores de la lista
print(f"Los valores de la lista son: {cuadrados[-10:]}")
