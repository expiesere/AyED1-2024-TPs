"""Ejercicio 8"""
import os

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

clear_screen()
impares = [x for x in range(100, 201) if x % 2 != 0]
"""
    -x for x in: Esta es la lista por compresion
    -range(100, 201): Secuencia de numeros de 100 a 200 inclusive
    -if x % 2 !0: Filtra todos los numeros impares, es decir; los que no son divisibles por 2
"""
print(impares)
