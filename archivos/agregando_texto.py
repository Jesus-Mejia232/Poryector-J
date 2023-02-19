#Agregando contenido al archivo txt
with open('archivos\\Jesus.txt','a',encoding='UTF-8') as archivo:
    #archivo.write('Hola, probando agregar texto al archivo con a de apend')
    #Usando un bucle para agregar varias líneas:
    for i in range(5): archivo.write(f"Línea {5} agregada\n")
    

#Con este metodo, podemos agregar más texto al archivo sin necesidad de eliminar el contenido que tenga
#El archivo
#La diferencia entre el write y el append es que el append no elimina los datos que tenga ya el 
#Archivo, la peculiaridad de append es que nos agrega de nueva cuenta el texto que contiene 
#Cada vez que se ejecuta