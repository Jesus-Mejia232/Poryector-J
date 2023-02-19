import csv

with open("archivos_remake\\archivos_csv\\leyendo_archivos_csv\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)