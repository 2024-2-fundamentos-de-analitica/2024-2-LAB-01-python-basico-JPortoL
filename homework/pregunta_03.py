"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    conteo = {}
    with open("files/input/data.csv", mode='r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            letra = fila[0]
            valor = int(fila[1])
            if letra in conteo:
                conteo[letra] += valor
            else:
                conteo[letra] = valor
    return sorted(conteo.items())   

if __name__ == "__main__":  
    print(pregunta_03())