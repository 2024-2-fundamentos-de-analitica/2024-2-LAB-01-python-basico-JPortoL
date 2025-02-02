"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    conteo = {}
    with open("files/input/data.csv", mode='r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            letra = fila[0]
            valor = int(fila[1])
            if letra in conteo:
                if valor > conteo[letra][0]:
                    conteo[letra] = (valor, conteo[letra][1])
                if valor < conteo[letra][1]:
                    conteo[letra] = (conteo[letra][0], valor)
            else:
                conteo[letra] = (valor, valor)
    return sorted([(k, v[0], v[1]) for k, v in conteo.items()])

if __name__ == "__main__":
    print(pregunta_05())
