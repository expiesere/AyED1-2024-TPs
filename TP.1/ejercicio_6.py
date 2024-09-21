"""Ejercicio 6"""


def concatenar_numeros(num1: int, num2: int) -> int:
    """
    Recibe dos numeros enteros positivos y devuelve el numero resultante de concatenar ambos.

    Pre:
        - num1 (int): Primer numero entero positivo.
        - num2 (int): Segundo numero entero positivo.

    Post:
        - int: Retorna el resultado de esos dos numeros juntos como si fuera una cadena.
    """
    digitos = 0  # Esta variable va contar la cantidad de digitos que tiene num2
    contar_digitos = num2  # Esta variable tiene el valor de num2 para no modificar el valor original de num2
    while contar_digitos > 0:  # Mientras el valor sea mayor a 0, entra a este bucle
        contar_digitos //= 10  # Divide esta variable por 10 y guarda el valor en la misma variable x cada iteracion
        digitos += 1  # Actua como contador de cada iteracion
    return (num1 * (10**digitos) + num2)  # Calcula el resultado de num1 multiplicando x 10 al numero de digitos en num2, eso crea un espacio de ceros para dar lugar a num2


def main() -> None:
    """
    Solicita al usuario dos numeros enteros positivos y muestra el numero concatenado.

    No retorna nada.
    """
    try:
        num1 = int(input("1° numero entero positivo: "))
        num2 = int(input("2° numero entero positivo: "))

        if num1 < 0 or num2 < 0:
            print("Error: Los numeros deben ser enteros positivos.")
            return

        resultado = concatenar_numeros(num1, num2)
        print(f"Los numeros {num1} y {num2} juntos forman: {resultado}")

    except ValueError:
        print("Error: Ingrese valores enteros positivos.")
    return None

if __name__ == "__main__":
    main()
