"""
Ejercicio 4

Todo programa Python es susceptible de ser interrumpido mediante la pulsación de 
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar 
un programa para imprimir los números enteros entre 1 y 100000, y que solicite 
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""

import os


def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.

    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None


def imprime_numeros() -> None:
    """
    Imprime los numeros del 1 al 100000. Si se presiona Ctrl-C, solicita confirmacion
    al usuario antes de detenerse.

    Except:
        KeyboardInterrupt: Si se presiona Ctrl-C y el usuario confirma la detencion.
    """
    try:
        for i in range(1, 100001):
            print(i)
    except KeyboardInterrupt:
        while True:
            try:
                confirm = input("\n¿Quieres detener el programa? (s/n): ")
                if confirm.lower() == "s":
                    print("Programa detenido.")
                    break
                else:
                    imprime_numeros()
            except KeyboardInterrupt:
                print("\nPrograma detenido forzosamente.")
                break
    return None


if __name__ == "__main__":
    clear_screen()
    imprime_numeros()
