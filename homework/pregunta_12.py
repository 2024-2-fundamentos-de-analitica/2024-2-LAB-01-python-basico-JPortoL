"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    conteo = {}
    with open("files/input/data.csv", mode='r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            letra = fila[0]
            columna_5 = fila[4].split(",")
            for valor in columna_5:
                valor = valor.split(":")
                valor = valor[1]
                if letra in conteo:
                    conteo[letra] += int(valor)
                else:
                    conteo[letra] = int(valor)
    return conteo

if __name__ == "__main__":  
    print(pregunta_12())