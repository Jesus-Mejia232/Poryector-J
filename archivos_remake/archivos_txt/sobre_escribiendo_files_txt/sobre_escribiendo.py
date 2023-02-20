"""with open("archivos_remake\\archivos_txt\\sobre_escribiendo_files_txt\\jesus.txt","w") as archivo:
    #archivo.write("Hola, probando a sobre escribir el contenido del archivo txt")
    archivo.write("\n")
    #print(archivo)
    for i in range(5):
        archivo.writelines(f"Linea {i+1} agregada \n")
        archivo.writelines(f"Lineaasdasdasd {i+1} agregada \n")

"""
#La "w" se agrega para tener el permiso de sobre escribir datos en los archivos
#with open("archivos_remake\\archivos_txt\\sobre_escribiendo_files_txt\\jesus.txt","w") as archivo:
#    for i in range(5):
#        archivo.write(f"Linea {i + 1} agregada\n")#El "+1" se pone para que se imprima la 5 fila en pantalla"""
        #archivo.write(f"Lineadsfsdfsd {i + 1} agregada\n")#El "+1" se pone para que se imprima la 5 fila en pantalla"""
#    archivo.writelines(["Hola maestro","Como va todo?\n","Bestia\n"])
#    archivo.writelines(["Excelente","maquina\n","Y a vos como te va?"])
#"Write" Es para agregar solamente una cadena de texto
#"Writelolinens"  Es para agregar una lista con cadenas de texto
#Si ponemos dos veces cualquiera de los dos metodos (write o writelines) es como si se acumularan,
#Lo más correcto si vamos a agregar una lista de cadenas es usar el writelines 

#Agregando en texto en bucle con write:
with open("archivos_remake\\archivos_txt\\sobre_escribiendo_files_txt\\jesus.txt","w") as archivo:
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"Agregando linea {i + 1}\n") 