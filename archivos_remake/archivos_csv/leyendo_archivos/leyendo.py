"""import csv

with open("archivos_remake\\archivos_csv\\leyendo_archivos_csv\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)# Con este  for estamos haciendo que nos muestre el archivo en pantalla, con una lista 
        #En cada fila
"""

"""import csv

with open("archivos_remake\\archivos_csv\\leyendo_archivos_csv\\datos.csv") as  archivo:
    reader = csv.reader(archivo)
    for row in reader: #La funcion "row" sirve para devolver el numero de filas en una referencia de celda
        print(row)#Con este for hacemos que nos muestre el archivo en pantalla, en forma de lista, de cada
        #Fila
"""


import csv
import csv  # Importamos las funciones del modulo "csv"
with open("archivos_remake\\archivos_csv\\leyendo_archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    print(archivo)

with open("archivos_remake\\archivos_csv\\leyendo_archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)  # Con esto hacemos que nos imprima en cada fila una lista

# Otra forma de leerlo es de la siguiente manera


with open("archivos_remake\\archivos_csv\\leyendo_archivos\\datos.csv", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    # Con este metodo(row) estamos que nos devuelva una lista en cada fila del archivo
    for row in reader:
        # La primer fila la interpreta como el nombre de las columnas, en caso de que se lleve a un
        print(row)
        # excel, lo interpreta de esa manera, lo demás lo interpreta como los datos de las columnas


with open("archivos_remake\\archivos_csv\\leyendo_archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
