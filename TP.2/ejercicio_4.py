"""Ejercicio 4"""
import random as rn

def eliminar_valores(lista_original, lista_a_eliminar):
    """Elimina los valores que se encuentren en las dos listas."""
    print(f"\nOriginal: {lista_original}")
    print(f"Lista de valores a eliminar: {lista_a_eliminar}")

    for valor in lista_a_eliminar:
        while valor in lista_original:
            lista_original.remove(valor)

    print(f"Resultado: {lista_original}")
    return None


def main():
    """Le solicita al usuario N cantidad de numeros para crear las listas"""

    # Solicitar al usuario la cantidad de numeros a generar
    cantidad_numeros = int(input("Ingrese la cantidad de numeros a generar: "))

    # Generar la lista original con numeros aleatorios
    lista_original = [rn.randint(1, 100) for i in range(cantidad_numeros)]

    # Generar la lista de valores a eliminar con numeros aleatorios
    cantidad_a_eliminar = int(input("Ingrese la cantidad de numeros a eliminar: "))
    lista_a_eliminar = [rn.randint(1, 100) for j in range(cantidad_a_eliminar)]

    # Llamar a la funcion para eliminar los valores
    eliminar_valores(lista_original, lista_a_eliminar)
    return None


if __name__ == "__main__":
    main()
