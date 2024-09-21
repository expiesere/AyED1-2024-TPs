"""Ejercicio 1"""


def mayor_estricto(a: int, b: int, c: int) -> int:
    """
    Evalua 3 numeros enteros positivos y devuelve el mayor valor unico o -1 si no existe.

    Pre:
    - a, b, c son numeros enteros positivos.

    Post:
    - Valor mayor unico encontrado.
    - -1 si mayor unico no existe.
    """
    max_val = max(a, b, c)

    contar = (a == max_val) + (b == max_val) + (c == max_val)

    if contar == 1:
        return max_val
    else:
        return -1


def main() -> None:
    """
    Solicita al usuario tres numeros enteros positivos e invoca la funcion 'mayor_estricto'
    para evaluar los numeros y encontrar un valor mayor unico.

    Pre:
        -Usuario ingresa 3 valores enteros positivos

    Post:
        -Imprime valor mayor unico o un mensaje si no encontro

    No retorna nada.
    """
    try:
        a = int(input("Primer numero entero positivo: "))
        b = int(input("Segundo numero entero positivo: "))
        c = int(input("Tercer numero entero positivo: "))
    except ValueError:
        print("Error: Se deben ingresar numeros enteros.")
        return

    resultado = mayor_estricto(a, b, c)
    if resultado != -1:
        print(f"El mayor valor unico es: {resultado}")
        return
    else:
        print("No existe un valor mayor unico.")

    return None


if __name__ == "__main__":
    main()
