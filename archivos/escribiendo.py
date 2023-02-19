# Poniendo la "w" le estamos pidiendo "permiso" al programa para poder sobreecribir el programa
with open("archivos\\Jesus.txt", "w", encoding="UTF-8") as archivo:
    # Reescribiendo el texto del archivo, #Con esta función podemos sobreescribir el texto del archivo "write"
    # Este metodo borra toda la información que tenga el archivo
    archivo.writelines("Sobreescribiendo el texto del archivo ")
    archivo.write("Algun texto por aquí\n")
    # Pero con el permiso "w" si no encuentra el archivo, lo crea
    #Escribiendo sobre el archivo de texto con "writelines"
    #archivo.writelines(["Hola jefe de jefes, como andas\n","Jesus"])
    print(archivo)
#Cuando está el permiso "w" sobre escribe lo que estaba en el archivo. Si se vuelve a usar
#No elimina lo anteriormente escrito con la misma funcion sin importar el operador que vaya ("writelines" o 
# "write")