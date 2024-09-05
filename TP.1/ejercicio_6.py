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
    return f"{num1}{num2}"


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
