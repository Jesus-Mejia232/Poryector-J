#Para ver si tenemos instalada la libreria "pandas" iremos a cmd(como admistrador)
#Y escribiremos las siguientes 3 alternativas:
#1)"Pip" 2)"py pip" 3)"py -m pip"  si muestra que no está instalada la librería, a continuación veremos como
#instalarla
#Pasos, para actualizar es el siguiente comando "python -m ensurepip --upgrade" y para instalarlo es:
#"python get-pip.py" o "py -m pip install pandas"

import pandas as pd

archivo = pd.read_csv("archivos_remake\\archivos_csv\\leyendo_archivos\\datos.csv")
print(archivo)