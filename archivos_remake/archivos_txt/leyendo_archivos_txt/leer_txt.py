#Leyendo de forma optima los archivos
with open("archivos_remake\\archivos_txt\\leyendo_archivos_txt\\jesus.txt",encoding="UTF-") as archivo:
    Archivo = archivo.read()
    print(Archivo)
#Procurar no tener el permiso "w" cuando estemos leyendo archivos, ese permiso
#elimina todos los datos que tenga ese archivo(Debido a que es para sobre escribir archivos
# y no para leerlos)