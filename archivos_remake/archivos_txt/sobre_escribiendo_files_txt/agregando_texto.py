#Agregando texto al archivo, el dato es que con el permiso "a" se agregara el texto nuevamente, cada vez
#Que se ejecute
with open("archivos_remake\\archivos_txt\\sobre_escribiendo_files_txt\\jesus.txt","a") as archivo:
    archivo.write("Jesus Mejia, el más capo de todos\n")
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"Linea {i+1} agregada\n")#Ojo que si no lleva el "nombre.write" no se agrega al archivo
        