"""Ejercicio 11"""
import os
from typing import List, Tuple

def clear_screen() -> None:
    """
    Esta funcion limpia la terminal del usuario.
    
    No retorna nada.
    """
    os.system("cls" if os.name == "nt" else "clear")
    return None

def registrar_pacientes() -> Tuple[List[int], List[int]]:
    """
    Registra los pacientes que ingresan a la clinica.

    Post:
        -tuple: Dos listas, una con los pacientes atendidos por 
        -urgencia y otra con los pacientes atendidos por turno.
    """
    urgencias = []
    turnos = []

    while True:
        numero_afiliado = int(input("Ingrese el numero de afiliado (o -1 para finalizar): "))
        if numero_afiliado == -1:
            break
        tipo_atencion = int(input("Ingrese 0 para urgencia o 1 para turno: "))
        if tipo_atencion == 0:
            urgencias.append(numero_afiliado)
        elif tipo_atencion == 1:
            turnos.append(numero_afiliado)
    return urgencias, turnos


def mostrar_listados(urgencias: List[int], turnos: List[int]) -> None:
    """
    Muestra los listados de pacientes atendidos por urgencia y por turno.

    Pre:
        -urgencias (list): Lista de pacientes atendidos por urgencia.
        -turnos (list): Lista de pacientes atendidos por turno.
    """
    print("\nPacientes atendidos por urgencia:")
    for paciente in urgencias:
        print(paciente)

    print("\nPacientes atendidos por turno:")
    for paciente in turnos:
        print(paciente)
    return None

def buscar_paciente(urgencias: List[int], turnos: List[int]) -> None:
    """
    Busca un numero de afiliado y cuenta cuantas veces fue atendido por turno y 
    cuántas por urgencia.

    Pre:
        -urgencias (list): Lista de pacientes atendidos por urgencia.
        -turnos (list): Lista de pacientes atendidos por turno.
    """
    while True:
        numero_afiliado = int(input("Ingrese el numero de afiliado a buscar (o -1 para finalizar): "))
        if numero_afiliado == -1:
            break
        atenciones_urgencia = urgencias.count(numero_afiliado)
        atenciones_turno = turnos.count(numero_afiliado)
        print(f"El paciente {numero_afiliado} fue atendido {atenciones_urgencia} veces por urgencia y {atenciones_turno} veces por turno.")
    return None


def main() -> None:
    """
    Funcion principal que coordina el registro, 
    muestra los listados y realiza la búsqueda de pacientes.
    
    No retorna nada.
    """
    clear_screen()
    urgencias, turnos = registrar_pacientes()
    mostrar_listados(urgencias, turnos)
    buscar_paciente(urgencias, turnos)
    return None

if __name__ == "__main__":
    main()
