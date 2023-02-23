import pandas as pd

df = pd.read_csv("archivos_remake\\archivos_csv\\leyendo_archivos\\datos.csv")

df2 = pd.read_csv("archivos_remake\\archivos_csv\\leyendo_archivos\\datos.csv")


# Concatenandno las dos df:
concatenado = pd.concat([df, df2])

# Ver las primeras 3 filas con head():
primeras_filas = df.head(3)

# Ver las ultimas 3 filas con tail():
ultimas_filas = df.tail(3)

# Accediendo a las filas y columnas totales:
filas_colums_totales = df.shape

filas_totales, columns_totales = df.shape  # NOTE Es una manera de desempaquetar
# print(filas_totales)
# print(columns_totales)


# Obteniendo los datos de una sola fila:
nombre = df.iloc[:, 0]
# print(nombre)

# Accediendo a todos los apellidos con iloc:
apellido = df.loc[:, "Apellido"]
# print(apellido)

# Obteniendo la data estadistica del dataframe:
# data_estadisitca = df.describe()
# print(data_estadisitca)

# Accediendo a los datos de la fila 3:
fila3 = df.loc[2, :]

fila2 = df.iloc[2, :]
fila = df.loc[:, "Apellido"]
# print(fila)
# Accediendo a filas con edad mayor a 30
fila4 = df.loc[df["Edad"] > 40, :]
print(fila4)
