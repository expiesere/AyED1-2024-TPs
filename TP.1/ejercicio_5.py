"""
Ejercicio 5


DATO DE COLOR

Números Triangulares:
    Un número triangular es un número que se puede representar como un triángulo equilátero. 
    Se obtiene sumando una secuencia de números naturales consecutivos comenzando desde 1. 
    Por ejemplo:
        -El número 1 es triangular porque es simplemente 1.
        -El número 3 es triangular porque 1 + 2 = 3.
        -El número 6 es triangular porque 1 + 2 + 3 = 6.
        -El número 10 es triangular porque 1 + 2 + 3 + 4 = 10.

Visualmente estos números forman triángulos:

1:    *

3:   * *
      *

6:  * * *
     * *
      *

10: * * * *
     * * *
      * *
       *

Números Oblongos:
    Un número oblongo (también conocido como número rectangular) es un número que se puede 
    obtener multiplicando dos números naturales consecutivos.
    Por ejemplo:
        -El número 2 es oblongo porque 1 * 2 = 2.
        -El número 6 es oblongo porque 2 * 3 = 6.
        -El número 12 es oblongo porque 3 * 4 = 12.
        -El número 20 es oblongo porque 4 * 5 = 20.

Visualmente estos números forman rectángulos:

2:  **

6:  ***
    ***

12: ****
    ****
    ****

20: *****
    *****
    *****
    *****
"""
import os

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

# Evalua si un numero ingresado por el usuario es oblongo
es_oblongo = lambda n: any(k * (k + 1) == n for k in range(1, n))

# Evalua si un numero ingresado por el usuario es triangular
es_triangular = lambda n: any(k * (k + 1) // 2 == n for k in range(1, n))


def main() -> None:
    """
    Le solicita al usuario un numero entero y evalua si
    el numero es 'triangular' o 'oblongo' con funciones lambda.

    No retorna nada.
    """
    clear_screen()
    try:
        numero = int(input("Ingrese un numero para evaluar: "))
    except ValueError:
        print("Error: Ingrese un numero entero.")
        return

    if es_oblongo(numero):
        print(f"El numero {numero} es oblongo.")
    else:
        print(f"El numero {numero} no es oblongo.")

    if es_triangular(numero):
        print(f"El numero {numero} es triangular.")
    else:
        print(f"El numero {numero} no es triangular.")
    return None


if __name__ == "__main__":
    main()
