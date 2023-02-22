# Poniendo la "w" le estamos pidiendo "permiso" al programa para poder sobreecribir el programa
with open("archivos\\Jesus.txt", "w", encoding="UTF-8") as archivo:
    # Reescribiendo el texto del archivo, #Con esta función podemos sobreescribir el texto del archivo "write"
    # Este metodo borra toda la información que tenga el archivo
    # archivo.write("Sobreescribiendo el texto del archivo ")
    # Pero con el permiso "w" si no encuentra el archivo, lo crea
    archivo.writelines("Hola jefe de jefes, como andás?")
    print(archivo)

# Escribiendo con "writeline"
#
