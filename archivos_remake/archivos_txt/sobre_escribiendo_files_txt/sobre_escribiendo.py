with open("archivos_remake\\archivos_txt\\sobre_escribiendo_files_txt\\jesus.txt","w") as archivo:
    #archivo.write("Hola, probando a sobre escribir el contenido del archivo txt")
    archivo.write("\n")
    print(archivo)
    for i in range(5):
        archivo.write(f"Linea {i+1} agregada \n")