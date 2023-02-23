# Si vamos a trabajar profesionalemnte, con analisis de datos
import pandas as pd

df = pd.read_csv(
    "archivos_remake\\archivos_csv\\leyendo_archivos\\datos.csv")  # name=["Nombre1","Nombre2","Nombre3","Nombre4"] Con esa funcion se cambian los encabezados

df2 = pd.read_csv(
    "archivos_remake\\archivos_csv\\leyendo_archivos\\datos.csv")
# print(df)

# Obteniendo los datos de la columna nombre:
# nombres = df["name"]
# print(df)


# df_ordenado_ascendente = df.sort_values("Edad")
# print(df_ordenado_ascendente)
# df_ordenado_descendente = df.sort_values("Edad", ascending=False)
# print(df_ordenado_descendente)

# Que es el slicing, sirve para ver elementos determinados de un alamcenador de valores, ejem:
# cadena = "0123456789"
# print(cadena[:])#Solo los dos puntos, imprimen todos los elementos en pantalla


# Concatenando los 2 dataframes
# df_concatenado = pd.concat([df, df2])
# print(df_concatenado)

# Accediendo a las primeras 3 filas con "head()":
# primeras_filas = df.head()  # "Head" Necesita parametros para imprimir la fila
# print(primeras_filas)

# Accediendo a las ultimas 3 filas con "tail()":
# utlimas_filas = df.tail(2)
# print(utlimas_filas)
# Esa es la unica limitante, que solo puede mostrar en pantalla las primeras, o ultiams filas


# accediendo a la cantidad de filas y columnas con shape:
# filas_y_columnas_totales = df.shape

# De esta formas estamos desempaquetando:
# filas_totales, columns_totales = df.shape

# print(
#    f"La cantidad de filas es: {filas_totales}, y la cantidad de columnas totales es: {columns_totales}")

# Obteniendo data estádistica del dataframe:
# df_info = df.describe()

# print(df_info)


# Accediendo a los valores especificos con loc:
# EL 1 valor será el número de la fila y el 2 valor será el nombre de la columna
# elemento_especifico = df.loc[2, "Edad"]
# print(elemento_especifico)

# Accediendo a los valores especificos con iloc(la i es de hecho de "index"):
# El 1 valor es el número de la fila y el 2 es el número del indice
# elemento_especifico2 = df.iloc[2, 2]
# print(elemento_especifico2)

# Accediendo a todos los valores de una fila o columna con ayuda del slicing
nombres = df.iloc[:, 0]
print(f"Los datos de la columna son: {nombres}")

# Accediendo a todos los datos de una fila
# Al usar el slicing solamente con los dos puntos se indica que tome todos los datos en respectivo
fila2 = df.loc[2, :]
print(f"Los datos de la fila 2 son: {fila2}")
