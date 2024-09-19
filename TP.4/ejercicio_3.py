"""Ejercicio 3"""



def obtener_claves(clave_maestra: str) -> tuple:
    """
    Obtiene las dos claves a partir de la clave maestra.

    La primera clave se construye con los digitos en posiciones impares de la clave maestra.
    La segunda clave se construye con los digitos en posiciones pares de la clave maestra.

    Pre:
        -clave_maestra (str): La clave maestra como una cadena de caracteres.

    Post:
        -tuple: Una tupla con las dos claves (clave1, clave2).
    """
    clave1 = ""
    clave2 = ""
    for i in range(len(clave_maestra)):
        if i % 2 == 0:
            clave1 += clave_maestra[i]
        else:
            clave2 += clave_maestra[i]
    return clave1, clave2


def main() -> None:
    """
    Funcion principal que solicita al usuario la clave maestra
    y muestra las dos claves obtenidas.
    """
    clave_maestra = input("Ingrese la clave maestra: ")
    clave1, clave2 = obtener_claves(clave_maestra)
    print(f"Clave 1: {clave1}")
    print(f"Clave 2: {clave2}")
    return None


if __name__ == "__main__":
    main()
