"""Ejercicio 4"""


def entero_a_romano(numero: int) -> str:
    """
    Convierte un numero entero entre 0 y 3999 a su representacion en
    numeros romanos.

    Pre:
        -numero (int): El numero entero a convertir.

    Post:
        -str: La representacióo del numero en numeros romanos.
    """
    if not 0 <= numero <= 3999:
        raise ValueError("El numero debe estar entre 0 y 3999")
    valores = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    resultado = ""
    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    return resultado


def main() -> None:
    """
    Funcion principal que solicita al usuario un
    numero entero y muestra su representación en numeros romanos.
    """
    numero = int(input("Ingrese un numero entero entre 0 y 3999: "))
    try:
        romano = entero_a_romano(numero)
        print(f"El numero {numero} en numeros romanos es: {romano}")
    except ValueError as e:
        print(e)
    main()


if __name__ == "__main__":
    main()


# RANGO DE VALORES MAYOR: Se deberian agregar mas simbolos romanos para representar
# valores mas grandes, la lista valores se ampliaria para incluir numeros mas grandes.

# RANGO DE VALORES EN NEGATIVO  : Los numeros romanos no tienen representacion de numeros
#   en negativo, pero se podria definir una convercion para representarlos... quizas agregando
#   simbolo negativo para representar que es un numero romano negativo.
