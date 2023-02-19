# Usando Open para abrir un archivo con una codificación universal (UFT-8)
archivo = open("archivos\\Jesus.txt", encoding="UTF-8")
# De codificacion a la hora de imprimir en pantalla, errores tales como mostrar letras raras cuando llevan tilde"
# A ese error se le llama problema de codificación

# archivo = archivo.read()
# Como hacer si lo que queremos es leer solamente una linea
# No muestra nada porque no lo hemos cerrado, cuando un archivo se lee, si
# linea1 = archivo_sin_leer.readlines()
# Lo queremos volver a leerlo tenemos que cerrarlo, una vez que se lee no se pude volver a lee(Por motivos de seguridad)
# print(linea1)


# Leer archivo completo:
# Archivo = archivo.read()

# Leer el archivo linea por linea con:
# ineas = archivo.readlines()
# print(lineas)


# Leer una sola linea del archivo:
# NOTE Tener cuidado al usar "Readline" porque con archivos grandes se puede consumir
linea = archivo.readline(2)
# Toda la ram de la pc
print(linea)

# Lo ultimo sería cerrar el archivo: NOTE es importante cerrar el programa porque sino se pueden perder datos
# Al cerrar el programa de forma inesperada. Tambien nos ayuda a evitar el problema que no nos permite abrir
# El archivo con otros programas, aparte que nos libera recursos(ram sobre todo) de la pc para ser usados con otros
# Archivos que necesitamos en ese momento
archivo.close()

# Si necesitamos abrir el archivo nuevamente, tendremos que hacer de nueva cuenta todo lo anterior
