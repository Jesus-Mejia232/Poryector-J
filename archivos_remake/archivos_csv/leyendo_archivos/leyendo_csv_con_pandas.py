# Para ver si tenemos instalada la libreria "pandas" iremos a cmd(como admistrador)
# Y escribiremos las siguientes 3 alternativas:
# 1)"Pip" 2)"py pip" 3)"py -m pip"  si muestra que no está instalada la librería, a continuación veremos como
# instalarla
# Pasos, para actualizar es el siguiente comando "python -m ensurepip --upgrade" y para instalarlo es:
# "python get-pip.py" o "py -m pip install pandas"


# Se pone como nombre "df" para saber que se trata de un "dataframe"
# Los dataframes, son estructuras de datos, bidimensionales similares a una hoja de calculo, al no
# Comportarse como un archivo, tiene su propia forma de accederse. Siempre los valores que van a tener
# Son 2 filas y columnas
import pandas as pd
df = pd.read_csv("archivos_remake\\archivos_csv\\leyendo_archivos\\datos.csv")
print(df["Nombre"])


# Hay que ir familiarizandose con jupyter Notebook
