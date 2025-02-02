"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    conteo = {}
    with open("files/input/data.csv", mode='r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            diccionario = fila[4]
            for par in diccionario.split(","):
                clave, valor = par.split(":")
                valor = int(valor)
                if clave in conteo:
                    if valor > conteo[clave][0]:
                        conteo[clave] = (valor, conteo[clave][1])
                    if valor < conteo[clave][1]:
                        conteo[clave] = (conteo[clave][0], valor)
                else:
                    conteo[clave] = (valor, valor)
    return sorted([(k, v[1], v[0]) for k, v in conteo.items()])

if __name__ == "__main__":  
    print(pregunta_06())