"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    with open("files/input/data.csv", mode='r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            suma += int(fila[1])  # Convertir a número y sumar
    return suma

if __name__ == "__main__":
    print(pregunta_01())