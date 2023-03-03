#Cambiar el tipo de dato de una columna
import pandas as pd 

df = pd.read_csv("problema_resoluciones//datos.csv",encoding="UTF-8")
print(df)

#Convertir a string los tipos de datos de una columna 
df["Edad"] = df["Edad"].astype(str)

#Mostrar el tipo de dato, del primer elemento de la columane edad  
print(f"La edad es\n{type(df['Edad'][1])}")

#Remplazando los datos con un determinado nombre, con uno escrito por parámetros
df["Apellido"].replace("Mejia","maquina",inplace=True)
print(df["Apellido"])

#Eliminando las filas con datos faltantes:
df = df.dropna()#"Axis=1"Sirve para poder eliminar columnas, se pone el número de índice de la columna
#Para eliminarla
print(df)

#Eliminando las filas con datos repetidos
df = df.drop_duplicates()
print(df)


#Creando un csv con el dataframe resultante(Limpio)
df.to_csv("problema_resoluciones//datos_limpios.csv")