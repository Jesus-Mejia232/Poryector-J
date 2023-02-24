# Cambiar el tipo de dato de una columna:
import pandas as pd

df = pd.read_csv("problemas_resoluciones\\datos.csv")
df['Edad'] = df['Edad'].astype(str)
print(type(df['Edad'][0]))

print(df['Edad'][1])
