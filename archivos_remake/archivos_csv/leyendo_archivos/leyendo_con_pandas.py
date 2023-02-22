# Si vamos a trabajar profesionalemnte, con analisis de datos
import pandas as pd

df = pd.read_csv(
    "archivos_remake\\archivos_csv\\leyendo_archivos\\datos.csv")  # Con esa funcion se cambian los encabezados

df2 = pd.read_csv(
    "archivos_remake\\archivos_csv\\leyendo_archivos\\datos.csv")
# print(df)

# Obteniendo los datos de la columna nombre:
# nombres = df["name"]
# print(df)


df_ordenado_ascendente = df.sort_values("Edad")
# print(df_ordenado_ascendente)
df_ordenado_descendente = df.sort_values("Edad", ascending=False)
# print(df_ordenado_descendente)

# Que es el slicing, sirve para ver elementos determinados de un alamcenador de valores, ejem:
# cadena = "0123456789"
# print(cadena[:])#Solo los dos puntos, imprimen todos los elementos en pantalla


# Concatenando los 2 dataframes
# df_concatenado = pd.concat([df, df2])
# print(df_concatenado)

# Accediendo a las primeras 3 filas:
primeras_filas = df.head()  # "Head" Necesita parametros para imprimir la fila
print(primeras_filas)

# Accediendo a las ultimas 3 filas
utlimas_filas = df.tail(2)
print(utlimas_filas)
# Esa es la unica limitante, que solo puede mostrar en pantalla las primeras, o ultiams filas

# Accediendo a la cantidad de Filas y columnas con shape:
filas_colums_totales = df.shape

filas_totales, colums_totales = df.shape  # Esta es una forma de desempaquetar

print(filas_totales)
