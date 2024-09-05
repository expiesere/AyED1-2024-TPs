"""Ejercicio 1"""

def mayor_estricto(a, b, c):
    """
    Evalua 3 numeros enteros positivos y devuelve el mayor valor unico o -1 si no existe.
    
    Pre:
    - a, b, c son enteros positivos.
    
    Post:
    - Devuelve el mayor valor si es único.
    - Devuelve -1 si no hay un valor mayor único.
    """
    max_val = max(a,b,c)

    contar = (a == max_val) + (b == max_val) + (c == max_val)

    if contar == 1:
        return max_val
    else:
        return -1
def main():
    """
    Solicita al usuario tres numeros enteros positivos e invoca la funcion mayor_estricto.

    Pre:
    - Los valores que se ingresan deben ser enteros positivos.

    Post:
    - Muestra el mayor valor unico o un mensaje si no existe.
    """

    a = int(input("Ingrese el primer numero entero positivo: "))
    b = int(input("Ingrese el segundo numero entero positivo: "))
    c = int(input("Ingrese el tercer numero entero positivo: "))

    resultado = mayor_estricto(a, b, c)

    if resultado != -1:
        print(f"El mayor valor unico es: {resultado}")
    else:
        print("No existe un valor mayor unico.")
    return None

if __name__ == "__main__":
    main()
