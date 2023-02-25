# Cambiar el tipo de dato de una columna:
import pandas as pd

df = pd.read_csv("problemas_resoluciones\\datos.csv")

# Convertir a string el tipo de dato de una columna
df['Edad'] = df['Edad'].astype(str)
print(df['Edad'][0])

# Mostrar el tipo de dato del primer elemento de la columna edad:
print(type(df['Edad'][1]))

# Remplazando un dato str por otro dato igual:
df["Apellido"].replace("Mejia", "Maquina", inplace=True)
print(df["Apellido"])
