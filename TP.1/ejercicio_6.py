"""Ejercicio 6"""


def concatenar_numeros(num1, num2):
    """
    Recibe dos numeros enteros positivos y devuelve el numero resultante de concatenar ambos.

    Pre:
        -Primer numero entero positivo
        -Segundo numero entero positivo

    Post:
        -Retorna el resultado de esos dos numeros juntos
    """
    digitos = 0  # Esta variable va contar la cantidad de digitos que tiene num2
    contar_digitos = num2  # Esta variable tiene el valor de num2 para no modificar el valor original de num2
    while contar_digitos > 0:  # Mientras el valor sea mayor a 0, entra a este bucle
        contar_digitos //= 10  # Divide esta variable por 10 y guarda el valor en la misma variable x cada iteracion
        digitos += 1  # Actua como contador de cada iteracion
    return (
        num1 * (10**digitos) + num2
    )  # Calcula el resultado de num1 multiplicando x 10 al numero de digitos en num2, eso crea un espacio de ceros para dar lugar a num2


def main():
    """
    Solicita al usuario dos numeros enteros positivos y muestra el numero concatenado.
    """
    try:
        num1 = int(input("Ingrese el primer número entero positivo: "))
        num2 = int(input("Ingrese el segundo número entero positivo: "))

        if num1 < 0 or num2 < 0:
            print("Error: Los numeros deben ser enteros positivos.")
            return

        resultado = concatenar_numeros(num1, num2)
        print(f"Los numeros {num1} y {num2} juntos forman: {resultado}")

    except ValueError:
        print("Error: Ingrese valores enteros positivos.")


if __name__ == "__main__":
    main()
